"""A shared native date picker for the student checklists."""
from homeassistant.components.date import DateEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([SchoolDate(entry.runtime_data, entry)])

class SchoolDate(CoordinatorEntity, DateEntity):
    _attr_has_entity_name = True
    _attr_name = "School day"
    _attr_icon = "mdi:calendar-edit"

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_school_date"
        self._attr_device_info = {"identifiers": {(DOMAIN, f"{entry.entry_id}_controls")}, "name": "VenvLearning", "manufacturer": "VenvLearning", "model": "School date controls"}

    @property
    def native_value(self):
        return self.coordinator.selected_date

    @property
    def extra_state_attributes(self):
        return {"tracks_today": not self.coordinator.entry.options.get("school_date")}

    async def async_set_value(self, value):
        await self.coordinator.async_select_date(value)
