import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_user_stories as url
async def get_user_stories(userid:str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url(user_id=userid), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
