from pydantic import BaseModel, Field
from typing import Optional


class EngagementToolModel(BaseModel):
    action_type:str=Field(...,description="action type")
    action:str=Field(...,description="action to perform")
    postId: Optional[int] = Field(None, description="post id to get info of")
    storyid: Optional[int] = Field(None, description="story id to get info of")
    commentid: Optional[int] = Field(None, description="comment id to get info of")
    comment: Optional[str] = Field(None, description="comment to post")
    page: Optional[int] = Field(None, description="page no. to use pagination")