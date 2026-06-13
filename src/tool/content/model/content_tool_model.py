from typing import Optional

from pydantic import BaseModel, Field


class ContentToolModel(BaseModel):
    content_type:str=Field(...,description="content domain type")
    action:str=Field(...,description="action to perform on the type domain")
    userid:Optional[str]=Field(None,description="user id to get data of")
    postid:Optional[int]=Field(None,description="post id to get info of")
    storyid:Optional[int]=Field(None,description="story id to get info of")
    page:Optional[int]=Field(None,description="page no. to use pagination")
