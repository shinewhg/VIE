from rocketchat_API.rocketchat import RocketChat

class Group:
    def __init__(self, rocket: RocketChat, name: str, id: str):
        self.name = name
        self.room_id = id
        self.rocket = rocket

    def get_history(self):
        return self.rocket.groups_history(self.room_id, count=50).json()
    
    def get_threads(self):
        history = self.get_history()
        threads = []

        for message in history['messages']:
            if 'tmid' not in message:
                threads.append(message)

        return threads
