from pydantic import BaseModel
class ChatRequestModel(BaseModel):
    conversation_id:str
    message_id:str
    message:str