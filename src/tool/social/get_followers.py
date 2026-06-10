import httpx
from src.constants.threadly_endpoints import GET_FOLLOWERS
from ..session import get_auth_headers



async def get_followers(userid:str):

    async with httpx.AsyncClient() as client:
        try:
            response=await client.get(GET_FOLLOWERS+f"/{userid}",headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()




