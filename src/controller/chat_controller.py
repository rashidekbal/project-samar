from http.client import responses

from fastapi import HTTPException
from ..services.chat import get_chat_history,generate_new_conversation,generate_chat
from ..model.new_conversation_request_model import NewConversationRequestModel
from ..model.chat_request_model import ChatRequestModel
async def new_chat_controller(body:NewConversationRequestModel):
    try:
        response=await generate_new_conversation(mid=body.message_id,message=body.message)
        return {"data":response}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=str(e))

async def chat_controller(body:ChatRequestModel):
    try:
        response=await generate_chat(conversation_id=body.conversation_id,mid=body.message_id,message=body.message)
        return {"data": response}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


async def chat_history_controller(thread_id:str):
    response=await get_chat_history(thread_id=thread_id)
    return {"history":response}