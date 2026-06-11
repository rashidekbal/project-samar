import httpx
from src.constants.threadly_endpoints import GET_MY_PROFILE
from src.tool.session import get_auth_headers


async def get_my_info():
    async with httpx.AsyncClient() as client:
        try:
            response= await  client.get(url=GET_MY_PROFILE,headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
