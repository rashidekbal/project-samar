import httpx
from src.constants.threadly_endpoints import GET_ALL_FOLLOW_REQUEST
from ..session import get_auth_headers



async def get_all_follow_request():
    async with httpx.AsyncClient() as client:
        try:
            response=await client.get(GET_ALL_FOLLOW_REQUEST,headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()




