from __future__ import annotations

import logging
from datetime import timedelta

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, INCIDENTS_API_URL, SCAN_INTERVAL_SECONDS, STATUS_API_URL

_LOGGER = logging.getLogger(__name__)


class ClaudeStatusCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, session: aiohttp.ClientSession) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=SCAN_INTERVAL_SECONDS),
        )
        self._session = session

    async def _async_update_data(self) -> dict:
        timeout = aiohttp.ClientTimeout(total=15)
        try:
            async with self._session.get(STATUS_API_URL, timeout=timeout) as resp:
                resp.raise_for_status()
                summary = await resp.json()
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error fetching Claude status: {err}") from err

        try:
            async with self._session.get(
                INCIDENTS_API_URL,
                timeout=timeout,
                params={"page[per_page]": 100},
            ) as resp:
                resp.raise_for_status()
                incidents_data = await resp.json()
            summary["all_incidents"] = incidents_data.get("incidents", [])
        except aiohttp.ClientError:
            _LOGGER.warning("Could not fetch Claude incident history; uptime sensors unavailable")
            summary["all_incidents"] = []

        return summary
