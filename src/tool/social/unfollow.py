import httpx
from src.constants.threadly_endpoints import UNFOLLOW_USERID
from ..name_value_pair_model import NameValuePairModel
from ..session import get_auth_headers



async def unfollow_user(followingid:str):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(UNFOLLOW_USERID,json={"nameValuePairs":{"followingid":followingid}},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()




