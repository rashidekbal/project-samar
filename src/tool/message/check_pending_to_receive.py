import httpx
from src.constants.threadly_endpoints import CHECK_PENDING_RECEIVE_MESSAGES
from src.tool.session import  get_auth_headers
async def check_pending_to_receive():
    async with httpx.AsyncClient() as client:
        try:
            response= await client.get(url=CHECK_PENDING_RECEIVE_MESSAGES,headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
