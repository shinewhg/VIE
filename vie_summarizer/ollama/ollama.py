import requests
from urllib.parse import urljoin

class AI():
    def __init__(self, url: str):
        self.url = url
        self.url_generate = urljoin(url, "/api/generate")

    def summarize_conversation(self, text: str):
        json = {
            "model": "llama3.2",
            "prompt": "Below is a post and replies (if any) regarding stocks. Summarize the conversation. If the content is empty then you can ignore it. Here is the conversation:\n" + text,
            "stream": False,
        }

        r = requests.post(self.url_generate, json=json, stream=False)
        r.raise_for_status()
        
        response_json = r.json()
        return response_json['response']
