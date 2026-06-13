from langchain_community.tools import DuckDuckGoSearchRun
from .auth.auth_tool import AuthTool
from .social.follow_tool_main import FollowTool
from .profile.profile_tool_main import ProfileTool
from .search.search_tool import SearchTool
from .content.content_tool_main import ContentTool
from .engagement.engagement_tool_main import EngagementTool
from .message.message_tool_main import MessageTool
tools=[AuthTool(),
       FollowTool(),
       ProfileTool(),
       SearchTool(),
       ContentTool(),
       EngagementTool(),
       MessageTool(),
       DuckDuckGoSearchRun()
       ]