from rocketchat_API.rocketchat import RocketChat

class RocketChatHelper:
    def __init__(self, rocket: RocketChat):
        self.rocket = rocket
        self.groups_list = rocket.groups_list().json()

    def chat_list_threads(self, room_id, **kwargs):
        """List threads."""
        return self.rocket.call_api_get(
            "chat.getThreadsList",
            rid=room_id,
            kwargs=kwargs,
        )

    def rooms_get_discussions(self, room_id, **kwargs):
        """Get Room Discussions."""
        return self.rocket.call_api_get(
            "rooms.getDiscussions",
            roomId=room_id,
            kwargs=kwargs,
        )

    def get_room_id(self, group_name):
        for group in self.groups_list['groups']:
            if group['fname'] == group_name:
                return group['_id']
        return None
    