import os
from requests import sessions
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import vie_summarizer.rocketchat.rocketchat as rocketchat

def main():
    pat_userid, pat_token = get_creds()

    with sessions.Session() as session:
        rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url='https://rc.seekingalpha.com', session=session)
        rocketChatHelper = rocketchat.RocketChatHelper(rocket)

        # rooms = ["VIE: Off-Topic & Trading", "Value Investor's Edge"]
        rooms_to_summarize = ["Value Investor's Edge"]
        for room_name in rooms_to_summarize:
            room_id = rocketChatHelper.get_room_id(room_name)
            if room_id is None:
                raise Exception("Room not found: " + room_name)

            threads = rocketChatHelper.chat_list_threads(room_id, count=2).json()['threads']

            print("Number of threads: " + str(len(threads)))
            pprint(threads)

def get_creds():
    return os.environ.get('ROCKETCHAT_PAT_USERID'), os.environ.get('ROCKETCHAT_PAT_TOKEN')
