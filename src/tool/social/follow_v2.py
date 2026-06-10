import httpx
from src.constants.threadly_endpoints import FOLLOW_USERID
from ..session import get_auth_headers



async def follow_user(followingid:str):

    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(FOLLOW_USERID,json={"nameValuePairs":{"followingid": followingid}},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()




