import httpx
from src.constants.threadly_endpoints import SEND_MESSAGE
from src.tool.session import  get_auth_headers
from src.utils.date_util import get_timestamp
from src.utils.uuid_generator import generate_uuid
async def send_message(replyToMessageId:str,senderProfilePic:str,senderName:str,senderUserId:str,receiver_uuid:str,senderUuid:str,type:str,message:str,postLink:str,postId:int):
    async with httpx.AsyncClient() as client:
        try:

            response= await client.post(url=SEND_MESSAGE,
                                        json={"nameValuePairs":
                                                  {"MsgUid":generate_uuid() ,
                                                   "replyToMessageId": replyToMessageId,
                                                   "senderProfilePic":senderProfilePic,
                                                   "senderName":senderName,
                                                   "senderUserId":senderUserId,
                                                   "senderUuid": senderUuid,
                                                   "receiverUuid": receiver_uuid,
                                                   "type":type,
                                                   "msg":message,
                                                   "timestamp":get_timestamp(),
                                                   "postLink": postLink,
                                                   "postId": postId  }}
                                        ,headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
