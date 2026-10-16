"""Connect using a revocable school-only key, without storing a parent password."""
import re
try:
    import probatio as vol
except ImportError:
    import voluptuous as vol
from aiohttp import ClientError
from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers import selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api import VenvClient, InvalidAuth
from .const import DOMAIN, CONF_URL, CONF_TOKEN

def schema(default_url="https://venvlearning.com"):
    return vol.Schema({
        vol.Required(CONF_URL, default=default_url): str,
        vol.Required(CONF_TOKEN): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)),
    })

class VenvLearningConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            url = user_input[CONF_URL].strip().rstrip('/')
            token = user_input[CONF_TOKEN].strip()
            if not re.fullmatch(r'https://[A-Za-z0-9.-]+(?::[0-9]+)?', url):
                errors[CONF_URL] = "invalid_url"
            elif not re.fullmatch(r'[a-f0-9]{64}', token):
                errors[CONF_TOKEN] = "invalid_auth"
            else:
                try:
                    await VenvClient(async_get_clientsession(self.hass), url, token).agenda()
                except InvalidAuth:
                    errors["base"] = "invalid_auth"
                except (ClientError, TimeoutError, ValueError, KeyError):
                    errors["base"] = "cannot_connect"
                else:
                    await self.async_set_unique_id(url)
                    if self.context.get("source") == "reauth":
                        return self.async_update_reload_and_abort(self._get_reauth_entry(), data_updates={CONF_URL:url, CONF_TOKEN:token})
                    self._abort_if_unique_id_configured()
                    return self.async_create_entry(title="VenvLearning", data={CONF_URL:url, CONF_TOKEN:token})
        return self.async_show_form(step_id="user", data_schema=schema(user_input.get(CONF_URL) if user_input else "https://venvlearning.com"), errors=errors)

    async def async_step_reauth(self, entry_data):
        return await self.async_step_user()
