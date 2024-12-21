import os
from requests import sessions
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import vie_summarizer.rocketchat.rocketchat as rocketchat
import vie_summarizer.time.time as time
import vie_summarizer.mongodb.mongodb as mongodb

def main():
    pat_userid, pat_token = get_creds()
    time_query = get_time_query()
    # time_query = mongodb.sanity_check()
    print(time_query)

    with sessions.Session() as session:
        rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url='https://rc.seekingalpha.com', session=session)
        rocketChatHelper = rocketchat.RocketChatHelper(rocket)

        # rooms = ["VIE: Off-Topic & Trading", "Value Investor's Edge"]
        rooms_to_summarize = ["Value Investor's Edge"]
        for room_name in rooms_to_summarize:
            room_id = rocketChatHelper.get_room_id(room_name)
            if room_id is None:
                raise Exception("Room not found: " + room_name)

            # pprint(rocketChatHelper.chat_list_threads(room_id, count=2, query=time_query).json())

            # threads = rocketChatHelper.chat_list_threads(room_id, count=50, sort='{"ts": 1}', query=time_query).json()['threads']
            # pprint(rocketChatHelper.rooms_get_discussions(room_id, count=2).json())
        #     threads = rocketChatHelper.chat_list_threads(room_id, count=20).json()['threads']

        #     print("Number of threads: " + str(len(threads)))
        #     for thread in threads:
        #         print(thread['u'])
        #         print(thread['ts'])
        #         print(thread['msg'])
        #         print("===================")
            
        #     # pprint(threads)

        # pprint(rocket.chat_get_message("izXV5VvIS0VXT8ntA").json())
        # pprint(rocket.chat_get_message("Ef5ja3hMhTgmkzq6w").json())

def get_creds():
    return os.environ.get('ROCKETCHAT_PAT_USERID'), os.environ.get('ROCKETCHAT_PAT_TOKEN')

def get_time_query():
    start_time, end_time = time.get_24h_window()
    return mongodb.get_time_interval_query("ts", start_time, end_time)
