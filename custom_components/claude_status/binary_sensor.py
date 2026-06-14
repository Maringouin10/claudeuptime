from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import ClaudeStatusCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: ClaudeStatusCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([ClaudeOperationalSensor(coordinator)])


class ClaudeOperationalSensor(
    CoordinatorEntity[ClaudeStatusCoordinator], BinarySensorEntity
):
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY
    _attr_unique_id = "claude_operational"
    _attr_name = "Operational"

    def __init__(self, coordinator: ClaudeStatusCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, "claude_ai")},
            name="Claude AI",
            manufacturer="Anthropic",
            model="Status Monitor",
            configuration_url="https://status.claude.com",
        )

    @property
    def is_on(self) -> bool | None:
        if not self.coordinator.data:
            return None
        indicator = self.coordinator.data.get("status", {}).get("indicator", "none")
        return indicator == "none"

    @property
    def extra_state_attributes(self) -> dict:
        if not self.coordinator.data:
            return {}
        status = self.coordinator.data.get("status", {})
        return {
            "indicator": status.get("indicator"),
            "description": status.get("description"),
        }
