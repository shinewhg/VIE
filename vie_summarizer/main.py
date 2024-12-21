import os
from requests import sessions
# from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import vie_summarizer.rocketchat.rocketchat as rocketchat
import vie_summarizer.time.time as time
import vie_summarizer.ai.ai as ai

def main():
    pat_userid, pat_token = get_creds()
    start_time, end_time = time.get_24h_window()
    ai_client = ai.AI("http://localhost:11434/api/generate")

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
            threads = rocketChatHelper.get_threads(messages)

            for id, thread in threads.items():
                summary = ai_client.summarize_conversation(thread.compile())
                print(summary)
                print("================")

def get_creds():
    return os.environ.get('ROCKETCHAT_PAT_USERID'), os.environ.get('ROCKETCHAT_PAT_TOKEN')
