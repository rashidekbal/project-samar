from typing import Any

import httpx
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from src.constants.threadly_endpoints import SEARCH
from src.tool.session import get_auth_headers


class SearchInput(BaseModel):
    query: str=Field(...,description="user or post to search for ")
class SearchTool(BaseTool):
    name:str = "search_tool"
    description:str ="""
    this tool will search for user or post on threadly platform
    """
    args_schema:type[BaseModel]=SearchInput
    def _run(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("use async tool")

    async def _arun(self, query: str, *args: Any, **kwargs: Any) -> Any:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url=SEARCH + f"?target={query}", headers=get_auth_headers())
                response.raise_for_status()
                if not response.content:
                    return {"error": "Empty response from server"}
                return response.json()

            except httpx.HTTPStatusError as err:
                if not err.response.content:
                    return {"error": f"HTTP {err.response.status_code} with empty body"}
                return err.response.json()

            except Exception as e:
                return {"error": str(e)}



