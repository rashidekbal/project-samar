import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_story_like_api,get_story_unlike_api
async def like_story(story_id:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_story_like_api(story_id=story_id), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
async def unlike_story(story_id:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_story_unlike_api(story_id=story_id), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
