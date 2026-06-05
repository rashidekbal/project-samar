from pydantic import BaseModel,Field
class Title(BaseModel):
    title: str=Field(description="conversation title")