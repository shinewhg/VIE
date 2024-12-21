# vie-summarizer
Daily summary of VIE RocketChat

Prerequisites:
- Python3
- [Ollama](https://ollama.com/download)

## To Run

### Generate Personal Access Token
From `rc.seekingalpha.com` web UI, top left, click your avatar > Preferences > Personal Access Tokens.

In drop-down choose `Ignore Two Factor Authentication`. Click Add. In your terminal set:
```
export ROCKETCHAT_PAT_USERID=<your user_id>
export ROCKETCHAT_PAT_TOKEN=<your token>
```

### Start Ollama
I'm using llama3.2 3B text only model. But it should be easy to try another. Just modify `vie_summarizer/ollama/ollama.py` in next step.
```
ollama run llama3.2
```

### Run python program
Clone this repo.
```
pip3 install -r requirements.txt
pip3 install .
vie_summarizer
```

A summary thread will be posted to VIE RocketChat `Value Investor's Edge` and `VIE: Off-Topic & Trading` channels.
