import httpx
from src.constants.threadly_endpoints import GET_PENDING_RECEIVE_MESSAGES
from src.tool.session import  get_auth_headers
async def get_pending_message_from(sender_uuid:str):
    async with httpx.AsyncClient() as client:
        try:
            response= await client.post(url=GET_PENDING_RECEIVE_MESSAGES,json={"nameValuePairs": {"senderUuid": sender_uuid  }},headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
