import httpx
from src.constants.threadly_endpoints import ACCEPT_FOLLOW_REQUEST
from ..name_value_pair_model import NameValuePairModel
from ..session import get_auth_headers



async def accept_follow_request(followerId:str):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(ACCEPT_FOLLOW_REQUEST,json={"nameValuePairs":{"followerId":followerId}},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()




