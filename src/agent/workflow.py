from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from .state import ChatState
from .nodes import chatNode
from src.tool.all_tools import tools
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

tools_node = ToolNode(tools)
_checkpointer = None
workflow = None

async def init_workflow():
    global _checkpointer, workflow
    _checkpointer = AsyncSqliteSaver.from_conn_string("checkpoints.db")
    checkPointer = await _checkpointer.__aenter__()

    graph = StateGraph(ChatState)
    graph.add_node("model", chatNode)
    graph.add_node("tools", tools_node)
    graph.add_conditional_edges("model", tools_condition)
    graph.add_edge("tools", "model")
    graph.add_edge(START, "model")
    graph.add_edge("model", END)

    workflow = graph.compile(checkpointer=checkPointer)
    return workflow

def get_workflow():
    if workflow is None:
        raise RuntimeError("Workflow not initialized")
    return workflow