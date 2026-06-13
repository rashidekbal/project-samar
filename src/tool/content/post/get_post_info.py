import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_post_info
async def get_post_details(postid:int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_post_info(post_id=postid), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
