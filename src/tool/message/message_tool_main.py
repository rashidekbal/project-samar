from typing import Any

from pydantic import BaseModel
from langchain_core.tools import BaseTool

from src.tool.message.model.message_tool_model import MessageToolModel


class MessageTool(BaseTool):
    name:str="message_tool"
    description:str="""
    threadly message tool
    action and required parameters
    """
    args_schema :type[BaseModel]=MessageToolModel
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        pass
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        pass