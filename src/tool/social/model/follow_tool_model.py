from typing import Optional
from pydantic import BaseModel, Field

class FollowToolModel(BaseModel):
    action: str = Field(..., description="Action to perform")
    followerId: Optional[str] = Field(None, description="ID of the follower")
    followingid: Optional[str] = Field(None, description="ID of the user to follow")
    userid: Optional[str] = Field(None, description="ID of the user")