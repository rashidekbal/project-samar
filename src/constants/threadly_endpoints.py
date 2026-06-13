import os
from dotenv import load_dotenv
load_dotenv()
base_url=os.getenv("BASE_URL")
# Auth endpoints
LOGIN_USERID=base_url+'/api/auth/login/userid'

# follower following related api's

FOLLOW_USERID=base_url+'/api/follow/follow/v2'
UNFOLLOW_USERID=base_url+'/api/follow/unfollow'

CANCEL_FOLLOW_REQUEST=base_url+'/api/follow/cancelFollowRequest'
ACCEPT_FOLLOW_REQUEST=base_url+'/api/follow/acceptFollowRequest'
REJECT_FOLLOW_REQUEST=base_url+'/api/follow/rejectFollowRequest'

GET_ALL_FOLLOW_REQUEST=base_url+'/api/follow/getAllFollowRequests'
GET_FOLLOWERS=base_url+'/api/follow/getFollowers'
GET_FOLLOWINGS=base_url+'/api/follow/getFollowings'


# profile related api's

GET_MY_PROFILE=base_url+"/api/users/getMyData"
GET_USER_PROFILE=base_url+"/api/users/getUser"
GET_USER_SUGGESTIONS=base_url+"/api/users/getUsers"
SEARCH=base_url+"/api/search"

# posts related api's
GET_IMAGE_FEED=base_url+"/api/posts/getImagePostsFeed"
GET_REELS_FEED=base_url+"/api/posts/getVideoPostsFeed"
def get_post_info(post_id:int):
    return  base_url + f"/api/posts/getPost/{post_id}"
def get_user_post_url(user_id:str,page:int=1):
    return base_url+f"/api/posts/getUserPosts/{user_id}?page={page}"
def get_liked_by_api_url(post_id:int):
    return base_url+f"/api/posts/{post_id}/likedby"
def get_shared_by_api_url(post_id:int):
    return base_url+f"/api/posts/{post_id}/sharedby"


# Stories related api's
GET_LOGGED_IN_USER_STORIES=base_url+"/api/story/getMyStories"
GET_STORIES_FEED=base_url+"/api/story/getStories"
def get_user_stories(user_id:str):
    return base_url+f"/api/story/getStories/{user_id}"

def get_story_viewed_by_api_url(story_id:int):
    return base_url+f"/api/story/{story_id}/viewedby"


# like related api's
def get_post_like_api(post_id:int):
    return base_url+f"/api/like/likePost/{post_id}"
def get_post_unlike_api(post_id:int):
    return base_url+f"/api/like/unlikePost/{post_id}"
def get_story_like_api(story_id:int):
    return base_url+f"/api/like/likeStory/{story_id}"
def get_story_unlike_api(story_id:int):
    return base_url+f"/api/like/unlikeStory/{story_id}"
def get_comment_like_api(comment_id:int):
    return base_url+f"/api/like/likeAComment/{comment_id}"
def get_comment_unlike_api(comment_id:int):
    return base_url+f"/api/like/unlikeAComment/{comment_id}"


# comment related api's
ADD_COMMENT=base_url+"/api/comment/addComment"
REMOVE_COMMENT=base_url+"/api/comment/removeComment"
def get_post_comment_api(post_id:int):
    return base_url+f"/api/comment/getComments/{post_id}"
def get_api_comment_reply(comment_id:int):
    return base_url+f"/api/comment/replyTo/{comment_id}"
def get_reply_of_comment_api(comment_id:int):
    return base_url+f"/api/comment/getCommentReplies/{comment_id}"

# message related api's

SEND_MESSAGE=base_url+"/api/messages/sendMessage"
CHECK_PENDING_RECEIVE_MESSAGES=base_url+"/api/messages/checkPendingMessages"
GET_PENDING_RECEIVE_MESSAGES=base_url+"/api/messages/getPendingMessages"

NOTIFY_MESSAGE_SEEN=base_url+"/api/messages/updateMessageDeliveryStatus"
GET_ALL_CHATS=base_url+"/api/messages/getAllChats"
DELETE_MESSAGE_FOR_ME="/api/messages/deleteMessageForMe"
UNSEND_MESSAGE=base_url+"/api/messages/unSendMessage"









