from pydantic import BaseModel

class NewConversationRequestModel(BaseModel):
    message_id:str
    message:str