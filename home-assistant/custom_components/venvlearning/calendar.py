"""A native read-only calendar of each student's subject tasks."""
from datetime import date, timedelta
from aiohttp import ClientError
from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .api import InvalidAuth
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = entry.runtime_data
    async_add_entities([StudentCalendar(coordinator, entry, student) for student in coordinator.data["students"]])

def event_for(item):
    day = date.fromisoformat(item["date"])
    return CalendarEvent(start=day, end=day+timedelta(days=1), uid=item["uid"],
        summary=("✓ " if item["completed"] else "")+item["summary"],
        description=("Complete" if item["completed"] else "Not yet complete")+"\n\n"+item["description"])

class StudentCalendar(CoordinatorEntity, CalendarEntity):
    _attr_has_entity_name = True
    _attr_name = "School calendar"
    _attr_icon = "mdi:calendar-check"

    def __init__(self, coordinator, entry, student):
        super().__init__(coordinator)
        self.student_id = student["id"]
        self._attr_unique_id = f"{entry.entry_id}_{self.student_id}_calendar"
        self._attr_device_info = {"identifiers": {(DOMAIN, self.student_id)}, "name": student["display_name"], "manufacturer":"VenvLearning", "model":f"Grade {student['grade']} school agenda"}

    @property
    def available(self):
        return super().available and self.coordinator.student(self.student_id) is not None

    @property
    def event(self):
        student = self.coordinator.student(self.student_id)
        return next((event_for(item) for item in (student or {}).get("items", []) if item["date"] >= self.coordinator.data["today"]), None)

    async def async_get_events(self, hass, start_date, end_date):
        # Calendar navigation can request months outside the minute-refresh cache.
        first, last = start_date.date(), end_date.date()
        items = []
        try:
            while first <= last:
                end = min(first + timedelta(days=91), last)
                result = await self.coordinator.client.agenda(first, end)
                student = next((s for s in result["students"] if s["id"] == self.student_id), None)
                for item in (student or {}).get("items", []):
                    event = event_for(item)
                    if event.end > start_date.date() and (event.start < end_date.date() or (event.start == end_date.date() and end_date.time().isoformat() != '00:00:00')):
                        items.append(event)
                first = end + timedelta(days=1)
        except (InvalidAuth, ClientError, TimeoutError, ValueError, KeyError) as error:
            raise HomeAssistantError("The school calendar could not load") from error
        return items
