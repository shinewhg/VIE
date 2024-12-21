import os
from requests import sessions
from urllib.parse import urljoin
# from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import vie_summarizer.rocketchat.rocketchat as rocketchat
import vie_summarizer.rocketchat.room as room
import vie_summarizer.time.time as time
import vie_summarizer.ollama.ollama as ollama

rocketchat_url = 'https://rc.seekingalpha.com'

def main():
    pat_userid, pat_token = get_creds()
    start_time, end_time = time.get_24h_window()
    ai_client = ollama.AI("http://localhost:11434")

    with sessions.Session() as session:
        rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url=rocketchat_url, session=session)
        rocketChatHelper = rocketchat.RocketChatHelper(rocket)

        rooms_to_summarize = [
            room.Room("Value Investor's Edge", "/group/value-investor-s-edge"),
            room.Room("VIE: Off-Topic & Trading", "/group/vie-off-topic-and-trading"),
        ]

        for curr_room in rooms_to_summarize:
            print("Room: " + curr_room.name)

            room_id = rocketChatHelper.get_room_id(curr_room.name)
            if room_id is None:
                raise Exception("Room not found: " + curr_room.name)
            
            room_url = urljoin(rocketchat_url, curr_room.url_prefix)
            
            print("Getting threads...")

            messages = rocket.groups_history(room_id, oldest=start_time, latest=end_time, count=1000).json()['messages']
            threads = rocketChatHelper.get_threads(messages)

            print("Summarizing threads...")

            for id, thread in threads.items():
                thread.add_summary(ai_client.summarize_conversation(thread.compile()))

            response = rocket.chat_post_message(f"Summarizing threads from {start_time} to {end_time}", room_id=room_id)
            summary_thread_id = response.json()['message']['_id']

            print("Posting summaries...")

            for id, thread in threads.items():
                message = "{}\n{}".format(thread.get_link(room_url), thread.summary)
                response = rocket.chat_post_message(message, room_id=room_id, tmid=summary_thread_id, tmshow=False)
            
            print("Done Room: " + curr_room.name + "\n=====")

def get_creds():
    return os.environ.get('ROCKETCHAT_PAT_USERID'), os.environ.get('ROCKETCHAT_PAT_TOKEN')

if __name__ == "__main__":
    main()
