import os
from requests import sessions
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import vie_summarizer.rocketchat.rocketchat as rocketchat
import vie_summarizer.time.time as time

def main():
    pat_userid, pat_token = get_creds()
    start_time, end_time = time.get_24h_window()

    with sessions.Session() as session:
        rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url='https://rc.seekingalpha.com', session=session)
        rocketChatHelper = rocketchat.RocketChatHelper(rocket)

        # rooms = ["VIE: Off-Topic & Trading", "Value Investor's Edge"]
        rooms_to_summarize = ["Value Investor's Edge"]
        for room_name in rooms_to_summarize:
            room_id = rocketChatHelper.get_room_id(room_name)
            if room_id is None:
                raise Exception("Room not found: " + room_name)
            
            messages = rocket.groups_history(room_id, oldest=start_time, latest=end_time, count=1000).json()['messages']
            rocketChatHelper.get_threads(messages)

def get_creds():
    return os.environ.get('ROCKETCHAT_PAT_USERID'), os.environ.get('ROCKETCHAT_PAT_TOKEN')
