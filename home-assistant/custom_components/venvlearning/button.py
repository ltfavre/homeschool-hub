"""Return both checklists to today's date and resume daily rollover."""
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([SchoolToday(entry.runtime_data, entry)])

class SchoolToday(CoordinatorEntity, ButtonEntity):
    _attr_has_entity_name = True
    _attr_name = "Today"
    _attr_icon = "mdi:calendar-today"

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_school_today"
        self._attr_device_info = {"identifiers": {(DOMAIN, f"{entry.entry_id}_controls")}, "name": "VenvLearning", "manufacturer": "VenvLearning", "model": "School date controls"}

    async def async_press(self):
        await self.coordinator.async_select_date(None)
