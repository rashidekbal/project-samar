from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from src.tool.auth.auth_tool import AuthTool
from src.tool.social.follow_tool_main import FollowTool
load_dotenv()
tools=[AuthTool(),FollowTool()]

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
).bind_tools(tools)


