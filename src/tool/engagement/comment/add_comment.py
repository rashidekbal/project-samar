
import httpx
from src.constants.threadly_endpoints import ADD_COMMENT
from src.tool.session import get_auth_headers
async def add_comment(postid:int,comment:str):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(ADD_COMMENT,json={"nameValuePairs":{"postid":postid,"comment":comment}},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
