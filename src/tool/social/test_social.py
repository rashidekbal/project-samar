import asyncio

# from ..auth.auth_tool import AuthTool
from .follow_tool_main import FollowTool
from src.tool.auth.auth_tool import AuthTool
auth_tool = AuthTool()
follow_tool=FollowTool()
async def runFunctino():
    # login=await auth_tool.ainvoke("")
    result = await follow_tool.ainvoke({
        "action": "cancel_follow",
        "followingid": "cutie_sammi"
    })

    print(result)

asyncio.run(runFunctino())