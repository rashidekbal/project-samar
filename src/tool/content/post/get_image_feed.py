import httpx
from src.tool.session import get_auth_headers
from src.constants.threadly_endpoints import GET_IMAGE_FEED
async def get_image_feed():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(GET_IMAGE_FEED, headers=get_auth_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as err:
            return err.response.json()
