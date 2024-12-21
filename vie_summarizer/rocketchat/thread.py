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
                s = '%s posted: %s' % (item['u']['name'], item['msg'])
            else:
                s = '%s replied: %s' % (item['u']['name'], item['msg'])

            messages.append(s)
        
        return '\n'.join(messages)

    def add_summary(self, summary):
        self.summary = summary
