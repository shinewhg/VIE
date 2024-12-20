import os
from requests import sessions
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
from . import groupslist
from . import group

def main():
    pat_userid=os.environ.get('ROCKETCHAT_PAT_USERID')
    pat_token=os.environ.get('ROCKETCHAT_PAT_TOKEN')

    with sessions.Session() as session:
        rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url='https://rc.seekingalpha.com', session=session)
        groups_list = groupslist.GroupsList(rocket)

        # rooms = ["VIE: Off-Topic & Trading", "Value Investor's Edge"]
        rooms_to_summarize = ["Value Investor's Edge"]
        for room_name in rooms_to_summarize:
            room_id = groups_list.get_room_id(room_name)
            if room_id is None:
                raise Exception("Room not found: " + room_name)
            
            room = group.Group(rocket, room_name, room_id)
            threads = room.get_threads()

            print("Number of threads: " + str(len(threads)))
            pprint(threads)
