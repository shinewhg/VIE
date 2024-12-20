from rocketchat_API.rocketchat import RocketChat
from pprint import pprint

class GroupsList:
    def __init__(self, rocket: RocketChat):
        self.groups_list = rocket.groups_list().json()

    def get_room_id(self, group_name):
        for group in self.groups_list['groups']:
            if group['fname'] == group_name:
                return group['_id']
        return None
