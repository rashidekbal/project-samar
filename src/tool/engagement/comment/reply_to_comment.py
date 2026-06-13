
import httpx
from src.constants.threadly_endpoints import get_api_comment_reply
from src.tool.session import get_auth_headers
async def reply_to_comment(post_id:int,comment_id,comment:str):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(get_api_comment_reply(comment_id=comment_id),json={"nameValuePairs":{"postId":post_id,"comment":comment}},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
