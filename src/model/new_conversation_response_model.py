
from .new_conversation_request_model import NewConversationRequestModel
class NewConversationResponseModel:
    def __init__(self,request:NewConversationRequestModel,conversation_id:str,generated_title,generated_message_id:str,response_id:str,response_message:str,time_stamp:str):
        self.received:NewConversationRequestModel= request
        self.generated:dict={
            "conversation_id":conversation_id,
            "generated_title":generated_title,
            "generated_message_id":generated_message_id,
            "response_id":response_id,
            "response_message":response_message,
            "time_stamp":time_stamp
        }


