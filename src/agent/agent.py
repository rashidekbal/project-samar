from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


