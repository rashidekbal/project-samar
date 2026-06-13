import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import GET_LOGGED_IN_USER_STORIES
async def get_my_stories():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(GET_LOGGED_IN_USER_STORIES, headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
