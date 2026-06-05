from ..agent.agent import model
from .state import ChatState

def chatNode(state:ChatState):
    reponse=model.invoke(state["messages"])
    return {"messages":[reponse]}