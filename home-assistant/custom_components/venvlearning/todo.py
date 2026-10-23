"""Subject checkboxes for the selected school date."""
from datetime import date
from aiohttp import ClientError
from homeassistant.components.todo import TodoItem, TodoItemStatus, TodoListEntity, TodoListEntityFeature
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .api import InvalidAuth
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = entry.runtime_data
    async_add_entities([StudentTodo(coordinator, entry, student) for student in coordinator.data["students"]]
        + [StudentAssignments(coordinator, entry, student) for student in coordinator.data["students"]])

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
            for item in (student or {}).get("items", []) if item["date"] == self.coordinator.data["selected_date"]]

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


def student_device(entry, student):
    return {"identifiers": {(DOMAIN, student["id"])}, "name": student["display_name"], "manufacturer": "VenvLearning", "model": f"Grade {student['grade']} school agenda"}

STATUS_TEXT = {"late": "Late", "due_today": "Due today", "assigned": "Due", "turned_in": "Turned in", "graded": "Graded"}

class StudentAssignments(CoordinatorEntity, TodoListEntity):
    """Teacher-created assignments. Checking one off turns it in on VenvLearning."""
    _attr_has_entity_name = True
    _attr_name = "Assignments"
    _attr_icon = "mdi:book-check-outline"
    _attr_supported_features = TodoListEntityFeature.UPDATE_TODO_ITEM

    def __init__(self, coordinator, entry, student):
        super().__init__(coordinator)
        self.student_id = student["id"]
        self._attr_unique_id = f"{entry.entry_id}_{self.student_id}_assignments"
        self._attr_device_info = student_device(entry, student)

    def _items(self):
        return (self.coordinator.student(self.student_id) or {}).get("assignments", [])

    @property
    def available(self):
        return super().available and self.coordinator.student(self.student_id) is not None

    @property
    def todo_items(self):
        out = []
        for item in self._items():
            subject = SUBJECTS.get(item["subject"], item["subject"])
            summary = f"{subject}: {item['summary']}"
            if item.get("status") == "graded" and item.get("score") is not None:
                summary += f" ({float(item['score']):g}/{float(item.get('possible') or item.get('points') or 0):g})"
            out.append(TodoItem(uid=item["uid"], summary=summary, due=date.fromisoformat(item["date"]),
                description=(STATUS_TEXT.get(item.get("status"), "") + ("\n\n" + item["description"] if item.get("description") else "")).strip(),
                status=TodoItemStatus.COMPLETED if item["completed"] else TodoItemStatus.NEEDS_ACTION))
        return out

    async def async_update_todo_item(self, item):
        original = next((task for task in self._items() if task["uid"] == item.uid), None)
        if original is None or item.status not in (TodoItemStatus.COMPLETED, TodoItemStatus.NEEDS_ACTION):
            raise HomeAssistantError("Only assignment checkmarks can be changed here")
        if original.get("locked"):
            raise HomeAssistantError("This assignment was already graded")
        try:
            await self.coordinator.client.complete_assignment(original, item.status == TodoItemStatus.COMPLETED)
        except (InvalidAuth, ClientError, TimeoutError, ValueError) as error:
            raise HomeAssistantError("The checkmark could not be saved to VenvLearning") from error
        await self.coordinator.async_request_refresh()

SUBJECTS = {"math": "Math", "ela": "ELA", "science": "Science", "social": "Social Studies", "spanish": "Spanish", "art": "Art", "life": "Human Sciences", "computer": "Computer Science", "skills": "Life Skills"}
