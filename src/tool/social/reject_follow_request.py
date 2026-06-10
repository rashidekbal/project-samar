import httpx
from src.constants.threadly_endpoints import REJECT_FOLLOW_REQUEST
from ..session import get_auth_headers



async def reject_follow_request(followerId:str):

    async with httpx.AsyncClient() as client:
        try:
            response=await client.delete(REJECT_FOLLOW_REQUEST+f"/{followerId}",headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()




