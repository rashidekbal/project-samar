import httpx
from src.constants.threadly_endpoints import GET_USER_PROFILE
from src.tool.session import get_auth_headers


async def get_user_profile(userid:str):
    async with httpx.AsyncClient() as client:
        try:
            url=GET_USER_PROFILE+"/"+userid
            response= await  client.get(url=url,headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
