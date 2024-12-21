class Thread():
    def __init__(self, thread_id, thread_messages: list):
        self.thread_id = thread_id
        self.thread_messages = thread_messages
        self.summary = None
    
    def append(self, message):
        self.thread_messages.append(message)
   
    def compile(self):
        messages = []
        for i, item in enumerate(self.thread_messages):
            if i == 0:
                s = '%s: %s' % (item['u']['name'], item['msg'])
            else:
                s = '%s: %s' % (item['u']['name'], item['msg'])

            messages.append(s)
        
        return '\n'.join(messages)

    def add_summary(self, summary):
        self.summary = summary

    def get_link(self, room_url: str) -> str:
        return f'{room_url}?msg={self.thread_id}'
