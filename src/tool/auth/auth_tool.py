import os
from langchain_core.tools import BaseTool
from dotenv import load_dotenv
import httpx
from src.constants.threadly_endpoints import LOGIN_USERID
from pydantic import BaseModel
from ..session import set_session_token
load_dotenv()
class AuthTool(BaseTool):
    name:str = "AuthTool"
    description:str = "authentication tool for logging in to threadly environment"
    args_schema:type[BaseModel]=None
    def _run(self):
        raise NotImplementedError("Use async")
    async def _arun(self,*args,**kwargs):
        userid=os.getenv("USERID")
        password=os.getenv("PASSWORD")
        async with httpx.AsyncClient() as client:
            try:
                response=await client.post(LOGIN_USERID,json={"nameValuePairs":{"userid":userid,"password":password}})
                response.raise_for_status()
                set_session_token(response.json()["token"])
                return response.json()
            except httpx.HTTPStatusError as e:
                return e.response.json()