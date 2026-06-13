import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import get_user_post_url
async def get_user_posts(userid:str,page:int=1):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(get_user_post_url(user_id=userid,page=page), headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
