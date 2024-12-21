from pprint import pprint
from collections import OrderedDict
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
    
    def organize_threads(self, messages):
        threads = OrderedDict()

        for message in reversed(messages):
            if "tmid" not in message:
                threads[message["_id"]] = [message]
            else:
                thread_id = message["tmid"]
                if thread_id in threads:
                    # Ignore messages that are part of older threads
                    threads[thread_id].append(message)

        
        print("Number of threads: " + str(len(threads)))
        for id, thread in threads.items():
            print(id + ", " + thread[0]['u']['name'] + ", " + thread[0]['ts'])
            for message in thread:
                print(message['msg'])
            print("===================")
    