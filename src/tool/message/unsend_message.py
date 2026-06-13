import httpx
from src.constants.threadly_endpoints import UNSEND_MESSAGE
from src.tool.session import get_auth_headers
async def unsend_message(msg_uid:str,receiver_uuid:str):
    async with httpx.AsyncClient() as client:
        try:
            response= await client.patch(url=UNSEND_MESSAGE,json={"nameValuePairs":{
                "MsgUid":msg_uid,
                "receiverUUid":receiver_uuid
            }},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
