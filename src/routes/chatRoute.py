from fastapi import APIRouter

from ..model.new_conversation_request_model import NewConversationRequestModel
from ..model.chat_request_model import ChatRequestModel
from ..controller.chat_controller import chat_controller,chat_history_controller,new_chat_controller
router=APIRouter()


@router.post("/newConversation")
async def chat(body:NewConversationRequestModel):
    return await new_chat_controller(body=body)
@router.post("/")
async def chat(body:ChatRequestModel):
    return await chat_controller(body=body)
@router.get("/history/{thread_id}")
async def get_chat_history(thread_id:str):
    return await chat_history_controller(thread_id=thread_id)
