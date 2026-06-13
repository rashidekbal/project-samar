import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_post_like_api,get_post_unlike_api
async def like_post(postid:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_post_like_api(post_id=postid), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
async def unlike_post(postid:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_post_unlike_api(post_id=postid), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
