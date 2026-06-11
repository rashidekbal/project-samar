from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel
from .model.profile_tool_model import ProfileToolModel
from .self_profile import get_my_info
from .user_profile import get_user_profile
from .suggested_users import get_user_suggestions
class ProfileTool(BaseTool):
    name:str = "user_profile_tool"
    description:str = """
    user profile tool for checking user details on threadly.
    actions and required params
    - get_self_profile : (no params)
    - get_user_profile : {userid}
    - get_users_suggestions : (no params)
    """
    args_schema:type[BaseModel]=ProfileToolModel
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("please use async version")
    async def _arun(self,action:str,userid:str=None ,*args: Any, **kwargs: Any) -> Any:
        match action:
            case "get_self_profile":
                return await get_my_info()
            case "get_user_profile":
                return await get_user_profile(userid)
            case "get_users_suggestions":
                return await get_user_suggestions()
            case _ :return "invalid action"
