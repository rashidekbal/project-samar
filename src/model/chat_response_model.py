
from .chat_request_model import ChatRequestModel
class ChatResponseModel:
    def __init__(self,request:ChatRequestModel,conversation_id:str,generated_message_id:str,response_id:str,response_message:str,time_stamp:str):
        self.received:ChatRequestModel = request
        self.generated={
            'conversation_id':conversation_id,
            'generated_message_id':generated_message_id,
            'response_id':response_id,
            'response_message':response_message,
            'time_stamp':time_stamp
        }

