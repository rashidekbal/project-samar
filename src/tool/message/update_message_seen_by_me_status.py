import httpx
from src.constants.threadly_endpoints import NOTIFY_MESSAGE_SEEN
from src.tool.session import  get_auth_headers
async def update_message_seen_status(sender_uuid:str,receiver_uuid:str):
    async with httpx.AsyncClient() as client:
        try:
            response= await client.post(url=NOTIFY_MESSAGE_SEEN,json={"nameValuePairs": {"senderUUid": sender_uuid  ,"receiverUUid":receiver_uuid }},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
