"""School-only API client. Never logs the connection key."""
from datetime import timedelta
from aiohttp import ClientSession, ClientTimeout
from homeassistant.util import dt as dt_util

class InvalidAuth(Exception):
    """The school connection was revoked or is invalid."""

class VenvClient:
    def __init__(self, session: ClientSession, url: str, token: str):
        self.session, self.url, self.token = session, url.rstrip('/'), token

    async def request(self, method, path, **kwargs):
        async with self.session.request(method, self.url + path,
                headers={"Authorization": "Bearer " + self.token},
                timeout=ClientTimeout(total=30), allow_redirects=False, **kwargs) as response:
            if response.status in (401, 403):
                raise InvalidAuth("The VenvLearning school key is invalid or revoked")
            response.raise_for_status()
            if response.status != 200:
                raise ValueError("Unexpected VenvLearning response")
            return await response.json()

    async def agenda(self, start=None, end=None):
        day = dt_util.now().date()
        return await self.request("GET", "/api/home-assistant/agenda", params={
            "start": (start or day - timedelta(days=7)).isoformat(),
            "end": (end or day + timedelta(days=35)).isoformat(),
        })

    async def complete(self, item, completed):
        return await self.request("POST", "/api/home-assistant/completion", json={
            "student_id": item["student_id"], "date": item["date"],
            "subject": item["subject"], "completed": completed,
        })

    async def complete_assignment(self, item, completed):
        return await self.request("POST", "/api/home-assistant/completion", json={
            "student_id": item["student_id"], "assignment_id": item["assignment_id"], "completed": completed,
        })
