"""Per-student sensors for the family dashboard: what to read now, what's due, and shared documents."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = entry.runtime_data
    entities = []
    for student in coordinator.data["students"]:
        entities += [ReadingNow(coordinator, entry, student), AssignmentsDue(coordinator, entry, student), SchoolDocuments(coordinator, entry, student)]
    async_add_entities(entities)

class StudentSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True
    # Lists and links change every refresh; keep them out of long-term history.
    _unrecorded_attributes = frozenset({"books", "up_next", "library_picks", "items", "documents", "prompts", "full_list", "pace"})
    key = ""

    def __init__(self, coordinator, entry, student):
        super().__init__(coordinator)
        self.student_id = student["id"]
        self._attr_unique_id = f"{entry.entry_id}_{self.student_id}_{self.key}"
        self._attr_device_info = {"identifiers": {(DOMAIN, self.student_id)}, "name": student["display_name"], "manufacturer": "VenvLearning", "model": f"Grade {student['grade']} school agenda"}

    @property
    def student(self):
        return self.coordinator.student(self.student_id) or {}

    @property
    def available(self):
        return super().available and self.coordinator.student(self.student_id) is not None

class ReadingNow(StudentSensor):
    _attr_name = "Reading now"
    _attr_icon = "mdi:book-open-page-variant"
    key = "reading_now"

    @property
    def native_value(self):
        books = (self.student.get("reading") or {}).get("books") or []
        core = next((b for b in books if b.get("role") == "core"), books[0] if books else None)
        return (core or {}).get("title", "No book assigned")[:250]

    @property
    def extra_state_attributes(self):
        r = self.student.get("reading") or {}
        books = r.get("books") or []
        core = next((b for b in books if b.get("role") == "core"), books[0] if books else {})
        return {"module": r.get("module_label"), "dates": r.get("dates"), "author": core.get("author"), "link": core.get("read_online"),
                "download": core.get("url"), "prompts": core.get("prompts", []), "books": books, "up_next": r.get("up_next"),
                "library_picks": r.get("library_picks", []), "pace": r.get("pace"), "full_list": r.get("full_list")}

class AssignmentsDue(StudentSensor):
    _attr_name = "Assignments due"
    _attr_icon = "mdi:clipboard-text-clock-outline"
    _attr_native_unit_of_measurement = "assignments"
    key = "assignments_due"

    @property
    def native_value(self):
        return sum(1 for a in self.student.get("assignments", []) if not a["completed"])

    @property
    def extra_state_attributes(self):
        items = [{"title": a["summary"], "subject": a["subject"], "due": a["date"], "status": a["status"], "points": a.get("points"),
                  "score": a.get("score"), "feedback": a.get("feedback"), "attachments": a.get("attachments", [])}
                 for a in self.student.get("assignments", [])]
        return {"late": sum(1 for a in items if a["status"] == "late"), "due_today": sum(1 for a in items if a["status"] == "due_today"), "items": items}

class SchoolDocuments(StudentSensor):
    _attr_name = "School documents"
    _attr_icon = "mdi:file-document-multiple-outline"
    key = "documents"

    @property
    def native_value(self):
        return len(self.student.get("documents", []))

    @property
    def extra_state_attributes(self):
        return {"documents": self.student.get("documents", [])}
