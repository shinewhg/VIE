class Thread():
    def __init__(self, thread_id, thread_messages: list):
        self.thread_id = thread_id
        self.thread_messages = thread_messages
    
    def append(self, message):
        self.thread_messages.append(message)

    def messages(self):
        return self.thread_messages
