# vie_summarizer
Daily summary of VIE RocketChat

The program does 3 things:
1. Scrape RocketChat and organizes each thread into a conversational string.
2. Sends the conversation to a LLM asking for a summary. The prompt is in `vie_summarizer/ollama/ollama.py`, and definitely needs work.
3. Posts the summaries to the RocketChat channels.

## Issues
- Does not parse images. Can be fixed with a AI model that recognizes images e.g. llama3.2 11B parameter model.
- Does not follow URLs. This is harder to solve, follow URL -> parse URL text -> add that to summary. What about paywalls?

## To Run

### Generate Personal Access Token
From `rc.seekingalpha.com` web UI, top left, click your avatar > Preferences > Personal Access Tokens.

In drop-down choose `Ignore Two Factor Authentication`. Click Add. In your terminal set:
```
export ROCKETCHAT_PAT_USERID=<your user_id>
export ROCKETCHAT_PAT_TOKEN=<your token>
```

Note: SeekingAlpha or RocketChat user/pass will not work. You must use PAT.

### Start Ollama
[Ollama](https://ollama.com/download)
I'm using llama3.2 3B text only model. But it should be easy to try another. Just modify `vie_summarizer/ollama/ollama.py` in next step.
```
ollama run llama3.2
```

### Run python program
Clone this repo. Install Python3.
```
pip3 install -r requirements.txt
pip3 install .
vie_summarizer
```

A summary thread will be posted to VIE RocketChat `Value Investor's Edge` and `VIE: Off-Topic & Trading` channels.

## References
Here is the [RocketChat REST API](https://developer.rocket.chat/apidocs/post-message). You will need it because the RocketChat python wrapper did not implement everything, but it is very easy to add more REST functionality.
