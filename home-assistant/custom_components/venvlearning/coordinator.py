"""Refresh agendas once a minute and share data between entities."""
import asyncio
from datetime import date, timedelta
import logging
from aiohttp import ClientError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed, HomeAssistantError
from .api import InvalidAuth

class VenvCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, entry, client):
        super().__init__(hass, logging.getLogger(__name__), name="VenvLearning",
            config_entry=entry, update_interval=timedelta(seconds=60), always_update=True)
        self.client = client
        self.entry = entry
        self._selection_lock = asyncio.Lock()

    @property
    def selected_date(self):
        """The last successfully loaded date, shared by both student lists."""
        return date.fromisoformat(self.data["selected_date"])

    async def _load(self, selected):
        # Keep the normal calendar window even when browsing a distant date.
        result = await self.client.agenda()
        selected = selected or result["today"]
        if not result["start"] <= selected <= result["end"]:
            chosen = date.fromisoformat(selected)
            extra = await self.client.agenda(chosen, chosen)
            for student in result["students"]:
                other = next((s for s in extra["students"] if s["id"] == student["id"]), None)
                student["items"].extend((other or {}).get("items", []))
                student["items"].sort(key=lambda item: (item["date"], item["subject"]))
        result["selected_date"] = selected
        return result

    async def _async_update_data(self):
        try:
            async with self._selection_lock:
                return await self._load(self.entry.options.get("school_date"))
        except InvalidAuth as error:
            raise ConfigEntryAuthFailed(str(error)) from error
        except (ClientError, TimeoutError, ValueError, KeyError) as error:
            raise UpdateFailed("VenvLearning agendas could not be refreshed") from error

    async def async_select_date(self, value):
        """Persist selection only after its tasks have loaded successfully."""
        async with self._selection_lock:
            selected = value.isoformat() if value else None
            try:
                result = await self._load(selected)
            except (InvalidAuth, ClientError, TimeoutError, ValueError, KeyError) as error:
                raise HomeAssistantError("The school date could not load. Please try again.") from error
            options = dict(self.entry.options)
            if selected:
                options["school_date"] = selected
            else:
                options.pop("school_date", None)
            self.hass.config_entries.async_update_entry(self.entry, options=options)
            self.async_set_updated_data(result)

    def student(self, student_id):
        return next((student for student in self.data["students"] if student["id"] == student_id), None)
