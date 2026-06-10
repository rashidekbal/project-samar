from ..agent.agent import model
from .state import ChatState
from langchain_core.messages import SystemMessage

def chatNode(state:ChatState):
    sysetem_prompt=SystemMessage(content="""your are a threadly user , reference your self with your user name u will find your details from loggin in your account,
    pretend to be a real user female , not a bot , talk and engage in human way""")
    final_message=[sysetem_prompt]+state["messages"]
    reponse=model.invoke(final_message)
    return {"messages":[reponse]}