"""Today's five subject checkboxes for each student."""
from datetime import date
from aiohttp import ClientError
from homeassistant.components.todo import TodoItem, TodoItemStatus, TodoListEntity, TodoListEntityFeature
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .api import InvalidAuth
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = entry.runtime_data
    async_add_entities([StudentTodo(coordinator, entry, student) for student in coordinator.data["students"]])

class StudentTodo(CoordinatorEntity, TodoListEntity):
    _attr_has_entity_name = True
    _attr_name = "Daily school tasks"
    _attr_icon = "mdi:clipboard-check-outline"
    _attr_supported_features = TodoListEntityFeature.UPDATE_TODO_ITEM

    def __init__(self, coordinator, entry, student):
        super().__init__(coordinator)
        self.student_id = student["id"]
        self._attr_unique_id = f"{entry.entry_id}_{self.student_id}_tasks"
        self._attr_device_info = {"identifiers": {(DOMAIN, self.student_id)}, "name": student["display_name"], "manufacturer":"VenvLearning", "model":f"Grade {student['grade']} school agenda"}

    @property
    def available(self):
        return super().available and self.coordinator.student(self.student_id) is not None

    @property
    def todo_items(self):
        student = self.coordinator.student(self.student_id)
        return [TodoItem(uid=item["uid"], summary=item["summary"], due=date.fromisoformat(item["date"]), description=item["description"],
            status=TodoItemStatus.COMPLETED if item["completed"] else TodoItemStatus.NEEDS_ACTION)
            for item in (student or {}).get("items", []) if item["date"] == self.coordinator.data["today"]]

    async def async_update_todo_item(self, item):
        student = self.coordinator.student(self.student_id)
        original = next((task for task in (student or {}).get("items", []) if task["uid"] == item.uid), None)
        if original is None or item.status not in (TodoItemStatus.COMPLETED, TodoItemStatus.NEEDS_ACTION):
            raise HomeAssistantError("Only school task checkmarks can be changed")
        if item.summary is not None and item.summary != original["summary"]:
            raise HomeAssistantError("Change lesson content in VenvLearning")
        try:
            await self.coordinator.client.complete(original, item.status == TodoItemStatus.COMPLETED)
        except (InvalidAuth, ClientError, TimeoutError, ValueError) as error:
            raise HomeAssistantError("The checkmark could not be saved to VenvLearning") from error
        await self.coordinator.async_request_refresh()
