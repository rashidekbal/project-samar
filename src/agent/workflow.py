from langgraph.graph import StateGraph,START,END
from .state import ChatState
from .nodes import chatNode
from langgraph.checkpoint.memory import InMemorySaver 
checkPointer=InMemorySaver()
graph=StateGraph(ChatState)
graph.add_node("model",chatNode)
graph.add_edge(START,"model")
graph.add_edge("model",END)

workflow=graph.compile(checkpointer=checkPointer)


