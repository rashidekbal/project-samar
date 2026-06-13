from typing import Any

from langchain_core.tools import BaseTool
from openai import BaseModel

from src.tool.content.model.content_tool_model import ContentToolModel
from src.tool.content.post.get_image_feed import get_image_feed
from src.tool.content.post.get_reel_feed import get_reels_feed
from src.tool.content.post.get_user_posts import get_user_posts
from src.tool.content.post.get_post_info import get_post_details
from src.tool.content.post.get_post_liked_by import get_post_liked_by_users
from src.tool.content.post.get_post_shared_by import get_post_shared_by_users
from src.tool.content.story.get_stories import get_stories_feed
from src.tool.content.story.get_user_stories import get_user_stories
from src.tool.content.story.get_my_stories import get_my_stories
from src.tool.content.story.get_story_viewed_by_info import get_story_viewed_by
async def handle_post_action(action:str,userid:str=None,postid:int=None,page:int=None):

    match action:

        case "get_image_feed":
            return await get_image_feed()
        case "get_video_feed":
            return await get_reels_feed()
        case "get_users_posts":
            return await get_user_posts(userid=userid,page=page)
        case "get_post":
            return await get_post_details(postid=postid)
        case "get_liked_by_info":
            return await get_post_liked_by_users(postid=postid)
        case "get_shared_by_info":
            return await get_post_shared_by_users(postid=postid)
        case _ :
            return "please provide a valid action"


async def handle_story_action(action:str,userid:str=None,storyid:int=None):
    match action:

        case "get_stories":
            return await get_stories_feed()
        case "get_user_stories":
            return await get_user_stories(userid=userid)
        case "get_my_stories":
            return await get_my_stories()
        case "get_story_viewed_by_info":
            return await get_story_viewed_by(storyid=storyid)
        case _:
            return "please provide a valid action"


class ContentTool(BaseTool):
    name:str = "content_tool"
    description:str = """
    threadly content tool  for getting posts and performing actions on them.
    content_type , action and required params:
    - post get_image_feed : (no params)
    - post get_video_feed : (no params)
    - post get_users_posts : {userid}
    - post get_post : {postid}
    - post get_liked_by_info : {postid}
    - post get_shared_by_info : {postid}
    
    - story get_stories : (no params)
    - story get_user_stories : {userid}
    - story get_my_stories : (no params)
    - story get_story_viewed_by_info : {storyid}
    """
    args_schema:type[BaseModel]=ContentToolModel
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return NotImplementedError("please use async call")
    async def _arun(self,content_type:str,action:str,userid:str=None,postid:int=None,storyid:int=None,page:int=None, *args: Any, **kwargs: Any) -> Any:
        match content_type:
            case "post":
                return await handle_post_action(action=action,userid=userid,page=page)
            case "story":
                return await handle_story_action(action=action,userid=userid,storyid=storyid)
            case _ :
                return "please provide a valid content_type"

