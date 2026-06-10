from typing import Any

from langchain_core.tools import BaseTool
from .model.follow_tool_model import FollowToolModel
from pydantic import BaseModel
from .follow_v2 import follow_user
from .unfollow import unfollow_user
from .cancel_follow_request import cancel_follow_request
from .reject_follow_request import reject_follow_request
from .accept_follow_request import accept_follow_request
from .get_all_follow_requests import get_all_follow_request
from .get_followers import get_followers
from .get_followings import get_followings
class FollowTool(BaseTool):
    name:str = "follow_tool"
    description:str = """
    Manages follow relationships on threadly.
    Actions and required params:
    - follow: {followingid}
    - unfollow: {followingid}
    - cancel_follow: {followingid}
    - reject_follow: {followerId}
    - accept_follow: {followerId}
    - get_all_follow_requests: (no params)
    - get_followers: {userid}
    - get_followings: {userid}
    """
    args_schema:type[BaseModel]=FollowToolModel
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("please use async version")

    async def _arun(self,action:str,followingid:str=None,followerId:str=None ,userid:str=None,*args: Any, **kwargs: Any) -> Any:
        match action:
            case "follow":
                return await follow_user(followingid)
            case "unfollow":
                return await unfollow_user(followingid)
            case "cancel_follow":
                return await cancel_follow_request(followingid)
            case "reject_follow":
                return await reject_follow_request(followerId)
            case "accept_follow":
                return await accept_follow_request(followerId)
            case "get_all_follow_requests":
                return await get_all_follow_request()
            case "get_followers":
                return await get_followers(userid)
            case "get_followings":
                return await get_followings(userid)
            case _ :
                return "please provide a valid action"
