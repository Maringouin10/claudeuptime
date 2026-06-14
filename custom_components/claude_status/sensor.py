from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import COMPONENT_STATUS_MAP, DOMAIN, INDICATOR_STATUS_MAP
from .coordinator import ClaudeStatusCoordinator


def _device_info() -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, "claude_ai")},
        name="Claude AI",
        manufacturer="Anthropic",
        model="Status Monitor",
        configuration_url="https://status.claude.com",
    )


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: ClaudeStatusCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SensorEntity] = [
        ClaudeOverallStatusSensor(coordinator),
        ClaudeIncidentCountSensor(coordinator),
    ]

    for component in coordinator.data.get("components", []):
        if not component.get("group", False):
            entities.append(
                ClaudeComponentSensor(
                    coordinator, component["id"], component["name"]
                )
            )

    async_add_entities(entities)


class ClaudeOverallStatusSensor(
    CoordinatorEntity[ClaudeStatusCoordinator], SensorEntity
):
    _attr_has_entity_name = True
    _attr_unique_id = "claude_overall_status"
    _attr_name = "Overall Status"
    _attr_icon = "mdi:robot"

    def __init__(self, coordinator: ClaudeStatusCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_device_info = _device_info()

    @property
    def native_value(self) -> str | None:
        if not self.coordinator.data:
            return None
        indicator = self.coordinator.data.get("status", {}).get("indicator", "none")
        return INDICATOR_STATUS_MAP.get(indicator, indicator)

    @property
    def extra_state_attributes(self) -> dict:
        if not self.coordinator.data:
            return {}
        status = self.coordinator.data.get("status", {})
        page = self.coordinator.data.get("page", {})
        return {
            "indicator": status.get("indicator"),
            "description": status.get("description"),
            "updated_at": page.get("updated_at"),
        }


class ClaudeIncidentCountSensor(
    CoordinatorEntity[ClaudeStatusCoordinator], SensorEntity
):
    _attr_has_entity_name = True
    _attr_unique_id = "claude_active_incidents"
    _attr_name = "Active Incidents"
    _attr_icon = "mdi:alert-circle-outline"
    _attr_native_unit_of_measurement = "incidents"

    def __init__(self, coordinator: ClaudeStatusCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_device_info = _device_info()

    @property
    def native_value(self) -> int | None:
        if not self.coordinator.data:
            return None
        return len(self.coordinator.data.get("incidents", []))

    @property
    def extra_state_attributes(self) -> dict:
        if not self.coordinator.data:
            return {}
        incidents = self.coordinator.data.get("incidents", [])
        return {
            "incidents": [
                {
                    "name": inc.get("name"),
                    "status": inc.get("status"),
                    "impact": inc.get("impact"),
                    "shortlink": inc.get("shortlink"),
                }
                for inc in incidents
            ]
        }


class ClaudeComponentSensor(
    CoordinatorEntity[ClaudeStatusCoordinator], SensorEntity
):
    _attr_has_entity_name = True
    _attr_icon = "mdi:server"

    def __init__(
        self,
        coordinator: ClaudeStatusCoordinator,
        component_id: str,
        component_name: str,
    ) -> None:
        super().__init__(coordinator)
        self._component_id = component_id
        self._attr_unique_id = f"claude_component_{component_id}"
        self._attr_name = component_name
        self._attr_device_info = _device_info()

    def _get_component(self) -> dict | None:
        if not self.coordinator.data:
            return None
        for component in self.coordinator.data.get("components", []):
            if component["id"] == self._component_id:
                return component
        return None

    @property
    def native_value(self) -> str | None:
        component = self._get_component()
        if not component:
            return None
        status = component.get("status", "unknown")
        return COMPONENT_STATUS_MAP.get(status, status.replace("_", " ").title())

    @property
    def extra_state_attributes(self) -> dict:
        component = self._get_component()
        if not component:
            return {}
        return {
            "status": component.get("status"),
            "description": component.get("description"),
            "updated_at": component.get("updated_at"),
        }
