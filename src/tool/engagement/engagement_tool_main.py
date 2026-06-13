from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from .comment.remove_comment import remove_comment
from .comment.add_comment import add_comment
from .comment.reply_to_comment import reply_to_comment
from .comment.get_comments import get_post_comments
from .comment.get_comment_replies import get_comments_replies
from .like.like_unlike_post import like_post,unlike_post
from .like.like_unlike_comment import like_comment,unlike_comment
from .like.like_unlike_story import like_story,unlike_story


from src.tool.engagement.model.engagement_tool_model import EngagementToolModel
async def handle_like_action(action:str,postid:int=None,commentid:int=None,storyid:int=None):
    match action:
        case "like_post":
            return await like_post(postid=postid)
        case "unlike_post":
            return await unlike_post(postid=postid)
        case "like_comment":
            return await like_comment(comment_id=commentid)
        case "unlike_comment":
            return await unlike_comment(comment_id=commentid)
        case "like_story":
            return await like_story(story_id=storyid)
        case "unlike_story":
            return await unlike_story(story_id=storyid)
        case _ :
            return "invalid action"
async def handle_comment_action(action:str,postid:int=None,commentid:int=None,comment:str=None):
    match action:
        case "add_comment":
            return await add_comment(postid=postid,comment=comment)
        case "remove_comment":
            return await remove_comment(post_id=postid,comment_id=commentid)
        case "get_comments":
            return await get_post_comments(post_id=postid)
        case "reply_to_comment":
            return await reply_to_comment(post_id=postid,comment_id=commentid,comment=comment)
        case "get_comment_replies":
            return await get_comments_replies(comment_id=commentid)
        case _:
            return "invalid action"




class EngagementTool(BaseTool):
    name:str = "content_engagement_tool"
    description:str ="""
    threadly engagement tool used to perform like actions and comments.
    action_type , action and required parameters
    - like like_post : {postId}
    - like unlike_post : {postId}
    - like like_comment : {commentid}
    - like unlike_comment : {commentid}
    - like like_story : {storyid}
    - like unlike_story : {storyid}
    
    - comment add_comment : {postId,comment}
    - comment remove_comment : {postId,commentid} 
    - comment get_comments : {postId}
    - comment reply_to_comment : {commentid,postId,comment}
    - comment get_comment_replies : {commentid}
    """
    args_schema:type[BaseModel]=EngagementToolModel
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return NotImplementedError("please use async version")
    async def _arun(self,action_type:str,action:str,postId:int=None,storyid:int=None,commentid:int=None,page:int=None,comment:str=None, *args: Any, **kwargs: Any) -> Any:
        match action_type:
            case "like":
                return await handle_like_action(action=action,postid=postId,commentid=commentid,storyid=storyid)
            case "comment":
                return await handle_comment_action(action=action,postid=postId,commentid=commentid,comment=comment)
            case _:
                return "invalid action_type"
