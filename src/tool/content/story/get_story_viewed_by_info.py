import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_story_viewed_by_api_url as url
async def get_story_viewed_by(storyid:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url(story_id=storyid), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
