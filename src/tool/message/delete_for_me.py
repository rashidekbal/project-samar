import httpx
from src.constants.threadly_endpoints import DELETE_MESSAGE_FOR_ME
from src.tool.session import get_auth_headers
async def delete_message_for_me(msg_uid:str,role:str):
    async with httpx.AsyncClient() as client:
        try:
            response= await client.patch(url=DELETE_MESSAGE_FOR_ME,json={"nameValuePairs":{
                "MsgUid":msg_uid,
                "Role":role
            }},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
