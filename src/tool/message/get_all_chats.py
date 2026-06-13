import httpx
from src.constants.threadly_endpoints import GET_ALL_CHATS
from src.tool.session import  get_auth_headers
async def unsend_message():
    async with httpx.AsyncClient() as client:
        try:
            response= await client.get(url=GET_ALL_CHATS,headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
