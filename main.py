import os
from requests import sessions
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat

email=os.environ.get('ROCKETCHAT_USER')
password=os.environ.get('ROCKETCHAT_PASSWORD')

pat_userid=os.environ.get('ROCKETCHAT_PAT_USERID')
pat_token=os.environ.get('ROCKETCHAT_PAT_TOKEN')

# with sessions.Session() as session:
#     rocket = RocketChat(user=email, password=password, server_url='https://rc.seekingalpha.com', session=session)
#     pprint(rocket.me().json())

with sessions.Session() as session:
    rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url='https://rc.seekingalpha.com', session=session)
    pprint(rocket.me().json())
    pprint(rocket.channels_list().json())
