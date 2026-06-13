from typing import Any

from pydantic import BaseModel
from langchain_core.tools import BaseTool

from src.tool.message.model.message_tool_model import MessageToolModel
from .check_pending_to_receive import check_pending_to_receive
from .get_pending_messages_from import get_pending_message_from
from .unsend_message import unsend_message
from .delete_for_me import delete_message_for_me
from .update_message_seen_by_me_status import update_message_seen_status
from .send_message import send_message
from .model.message_type import MessageType

class MessageTool(BaseTool):
    name:str="message_tool"
    description:str="""
    threadly message tool
    action and required parameters
    - send_message :{replyToMessageId,senderProfilePic,senderName,senderUserId,senderUuid,receiverUuid,type,msg,postLink,postId} //used to send message
    - check_pending_to_receive : (no params) //used to check if any message there to receive from any user
    - get_pending_messages_from : {senderUuid} //get pending message from any particular user
    - update_message_seen_by_me_status : {senderUUid,receiverUUid} //notify sender that their message has been seen
    - get_all_chats : (no params) //get all chats with all users till date
    - delete_message_for_me :{MsgUid,role} //delete a message from my side
    - unsend_message : {MsgUid,receiverUUid} //unsend a message
    
    """
    args_schema :type[BaseModel]=MessageToolModel
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return NotImplementedError("use async tool")
    async def _arun(self,action:str,
                    replyToMessageId:str=None,
                    senderProfilePic:str=None,
                    senderName:str=None,
                    senderUserId:str=None,
                    senderUuid:str=None,
                    MsgUid:str=None,
                    receiverUuid:str=None,
                    type:MessageType=None,
                    msg:str=None,
                    postLink:str=None,
                    postId:int=None,
                    role:str=None,
                    *args: Any,
                    **kwargs: Any) -> Any:
        match action:
            case "unsend_message":
                return await unsend_message(msg_uid=MsgUid,receiver_uuid=receiverUuid)
            case "delete_message_for_me":
                return await delete_message_for_me(msg_uid=MsgUid,role=role)
            case "update_message_seen_by_me_status":
                return await update_message_seen_status(sender_uuid=senderUuid,receiver_uuid=receiverUuid)
            case "get_pending_messages_from":
                return await get_pending_message_from(sender_uuid=senderUuid)
            case "check_pending_to_receive":
                return await check_pending_to_receive()
            case "send_message":
                return await send_message(replyToMessageId=replyToMessageId,
                                          senderProfilePic=senderProfilePic,
                                          senderName=senderName,
                                          senderUserId=senderUserId,
                                          senderUuid=senderUuid,
                                          receiver_uuid=receiverUuid,
                                          type=type,
                                          message=msg,
                                          postLink=postLink,
                                          postId=postId)
            case _ :
                return "invalid action"
