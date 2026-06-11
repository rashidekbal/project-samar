from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from src.tool.all_tools import tools
load_dotenv()


model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
).bind_tools(tools)


