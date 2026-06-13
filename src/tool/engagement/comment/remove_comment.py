import httpx
from src.constants.threadly_endpoints import REMOVE_COMMENT
from src.tool.session import get_auth_headers
async def remove_comment(post_id:int,comment_id:int):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(REMOVE_COMMENT,json={"nameValuePairs":{"postid":post_id,"commentid":comment_id}},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
