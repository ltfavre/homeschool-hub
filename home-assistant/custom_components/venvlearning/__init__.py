"""Native student calendars and daily checklists for VenvLearning."""
from homeassistant.const import Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api import VenvClient
from .coordinator import VenvCoordinator
from .const import CONF_URL, CONF_TOKEN

PLATFORMS = [Platform.CALENDAR, Platform.TODO]

async def async_setup_entry(hass, entry):
    client = VenvClient(async_get_clientsession(hass), entry.data[CONF_URL], entry.data[CONF_TOKEN])
    coordinator = VenvCoordinator(hass, entry, client)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass, entry):
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
