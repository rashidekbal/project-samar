from datetime import datetime

from ..model.chat_request_model import ChatRequestModel
from ..model.chat_response_model import ChatResponseModel
from ..model.new_conversation_response_model import NewConversationResponseModel,NewConversationRequestModel
from ..agent.structured_models.title_generator_model import title_generator_model
from ..agent.workflow import get_workflow
from langchain_core.messages import HumanMessage
from ..utils.uuid_generator import generate_uuid
async def generate_new_conversation(mid:str,message:str):
    try:
        conversation_id=generate_uuid()
        generated_title= title_generator_model.invoke(f"generate a conversation title based on given message : '{message}' ")
        generated_title=generated_title.title
        config={"configurable":{"thread_id":conversation_id}}
        response=await get_workflow().ainvoke({"messages":[HumanMessage(content=message)]},config=config)
        generated_message_id = response["messages"][-2].id
        response_id= response["messages"][-1].id
        response_message= response["messages"][-1].content
        return NewConversationResponseModel(request=NewConversationRequestModel(message_id=mid,message=message),
                                            conversation_id=conversation_id,
                                            generated_title=generated_title,
                                            generated_message_id=generated_message_id,
                                            response_id=response_id,
                                            response_message=response_message,
                                            time_stamp=str(datetime.now())
                                            )
    except Exception as e:
        raise e




async def generate_chat(conversation_id:str,mid:str,message:str):
   try:
       config = {"configurable": {
           "thread_id": conversation_id
       }}
       response = await get_workflow().ainvoke({"messages": [HumanMessage(content=message)]}, config=config)
       generated_message_id = response["messages"][-2].id
       response_id = response["messages"][-1].id
       response_message = response["messages"][-1].content
       return ChatResponseModel(request=ChatRequestModel(conversation_id=conversation_id,message_id=mid,message=message),
                                conversation_id=conversation_id,
                                generated_message_id=generated_message_id,
                                response_id=response_id,
                                response_message=response_message,
                                time_stamp=str(datetime.now())
                                )
   except Exception as e:
       raise e
async def get_chat_history(thread_id:str):
    config={"configurable":{
        "thread_id":thread_id
    }}
    response=get_workflow().get_state(config=config)
    return response[0]