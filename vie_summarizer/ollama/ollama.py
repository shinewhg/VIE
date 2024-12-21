import requests
from urllib.parse import urljoin
from pprint import pprint

class AI():
    def __init__(self, url: str):
        self.url = url
        self.url_generate = urljoin(url, "/api/generate")

    def summarize_conversation(self, text: str):
        json = {
            "model": "llama3.2",
            "prompt": "Please summarize the post and any replies in under 5 sentences. If you cannot summarize it, say Cannot Summarize. Here is the post and any replies:\n" + text,
            # "prompt": "Why is the sky blue?",
            "stream": False,
        }

        r = requests.post(self.url_generate, json=json, stream=False)
        r.raise_for_status()
        
        response_json = r.json()
        return response_json['response']
