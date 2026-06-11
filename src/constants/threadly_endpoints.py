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


