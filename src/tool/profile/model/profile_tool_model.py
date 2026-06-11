from typing import Optional

from pydantic import BaseModel, Field


class ProfileToolModel(BaseModel):
    action: str = Field(...,description="action to perform")
    userid: Optional[str] = Field(None,description="userid of user")