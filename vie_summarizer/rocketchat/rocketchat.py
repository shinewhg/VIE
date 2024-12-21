from pprint import pprint
from collections import OrderedDict
from vie_summarizer.rocketchat.thread import Thread
from rocketchat_API.rocketchat import RocketChat

class RocketChatHelper():
    def __init__(self, rocket: RocketChat):
        self.rocket = rocket
        self.groups_list = rocket.groups_list().json()

    def get_room_id(self, group_name):
        for group in self.groups_list['groups']:
            if group['fname'] == group_name:
                return group['_id']
        return None
    
    def get_threads(self, messages: list):
        threads = OrderedDict()

        for message in reversed(messages):
            tmid = message.get("tmid")
            if tmid is None:
                threads[message["_id"]] = Thread(message["_id"], [message])
            else:
                thread = threads.get(tmid)
                if thread is None:
                    # Ignore messages that are part of older threads
                    continue

                thread.append(message)
        
        print("Number of threads: " + str(len(threads)))
        for id, thread in threads.items():
            thread_messages = thread.messages()
            print(id + ", " + thread_messages[0]['u']['name'] + ", " + thread_messages[0]['ts'])
            for message in thread_messages:
                print(message['msg'])
            print("===================")
    