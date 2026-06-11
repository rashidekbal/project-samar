import httpx
from src.constants.threadly_endpoints import GET_USER_SUGGESTIONS
from src.tool.session import get_auth_headers


async def get_user_suggestions():
    async with httpx.AsyncClient() as client:
        try:
            response= await  client.get(url=GET_USER_SUGGESTIONS,headers=get_auth_headers())
            response.raise_for_status()
            # Guard against empty response
            if not response.content:
                return {"error": "Empty response from server"}

            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
