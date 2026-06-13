import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_comment_like_api,get_comment_unlike_api
async def like_comment(comment_id:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_comment_like_api(comment_id=comment_id), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
async def unlike_comment(comment_id:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_comment_unlike_api(comment_id=comment_id), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
