from typing import Optional

from pydantic import BaseModel, Field

from src.tool.message.model.message_type import MessageType
from .constant import ActionMaker


class MessageToolModel(BaseModel):
    action:str=Field(...,description="action perform")
    replyToMessageId:Optional[str]=Field(None,description="id of message to which the repy is being made")
    senderProfilePic:Optional[str]=Field(None,description="sender profile pic")
    senderName:Optional[str]=Field(None,description="sender username")
    senderUserId:Optional[str]=Field(None,description="Sender userid")
    senderUuid:Optional[str]=Field(None,description="sender uuid unique user id")
    receiverUuid:Optional[str]=Field(None,description="receiver uuid unique user id")
    type:Optional[MessageType]=Field(None,description="message type")
    msg:Optional[str]=Field(None,description="message content in text")
    timestamp:Optional[str]=Field(None,description="message creation timestamp")
    postLink:Optional[str]=Field(None,description="post link")
    postId:Optional[int]=Field(None,description="post of post which is being sent")
    role:Optional[ActionMaker]=Field(None,description="role of action maker")
    MsgUid:Optional[str]=Field(None,description="message unique id")