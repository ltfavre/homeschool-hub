"""Refresh agendas once a minute and share data between entities."""
from datetime import timedelta
import logging
from aiohttp import ClientError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed
from .api import InvalidAuth

class VenvCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, entry, client):
        super().__init__(hass, logging.getLogger(__name__), name="VenvLearning",
            config_entry=entry, update_interval=timedelta(seconds=60), always_update=True)
        self.client = client

    async def _async_update_data(self):
        try:
            return await self.client.agenda()
        except InvalidAuth as error:
            raise ConfigEntryAuthFailed(str(error)) from error
        except (ClientError, TimeoutError, ValueError, KeyError) as error:
            raise UpdateFailed("VenvLearning agendas could not be refreshed") from error

    def student(self, student_id):
        return next((student for student in self.data["students"] if student["id"] == student_id), None)
