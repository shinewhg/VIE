import os
from requests import sessions
from urllib.parse import urljoin
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import vie_summarizer.rocketchat.rocketchat as rocketchat
import vie_summarizer.rocketchat.room as room
import vie_summarizer.time.time as time
# import vie_summarizer.ollama.ollama as ollama
import vie_summarizer.pdf.pdf as pdf
import google.generativeai as genai
import base64

rocketchat_url = 'https://rc.seekingalpha.com'

def main():
    pat_userid, pat_token, gemini_api_key = get_creds()
    genai.configure(api_key=gemini_api_key)

    start_time, end_time = time.get_24h_window()
    # ai_client = ollama.AI("http://localhost:11434")

    with sessions.Session() as session:
        rocket = RocketChat(user_id=pat_userid, auth_token=pat_token, server_url=rocketchat_url, session=session)
        rocketChatHelper = rocketchat.RocketChatHelper(rocket)

        rooms_to_summarize = [
            room.Room("Value Investor's Edge", "/group/value-investor-s-edge"),
            room.Room("VIE: Off-Topic & Trading", "/group/vie-off-topic-and-trading"),
        ]

        for curr_room in rooms_to_summarize:
            print("Room: " + curr_room.name)

            room_id = rocketChatHelper.get_room_id(curr_room.name)
            if room_id is None:
                raise Exception("Room not found: " + curr_room.name)
            
            room_url = urljoin(rocketchat_url, curr_room.url_prefix)
            
            print("Getting threads...")

            messages = rocket.groups_history(room_id, oldest=start_time, latest=end_time, count=1000).json()['messages']
            threads = rocketChatHelper.get_threads(messages)

            print("Generating PDF...")

            doc = pdf.PDF()
            for id, thread in threads.items():
                # doc.add_thread_start()
                doc.add_thread(thread, rocketchat_url)
                
                # doc.add_thread_end()
                # doc.add_page_break()

            pdf_name = f"./generated/{curr_room.name}-{start_time}.pdf"
            doc.generate_pdf(pdf_name)

            print("Summarizing threads...")

            model = genai.GenerativeModel("gemini-1.5-flash")
            doc_path = pdf_name

            # Read and encode the local file
            with open(doc_path, "rb") as doc_file:
                doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

            prompt = "The following is a chat on shipping stocks. Please summarize the key points, highlighting details and numbers when appropriate."

            response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])

            summary = response.text
            print(summary)

            # print("Posting summaries...")

            # response = rocket.chat_post_message(f"Summarizing threads from {start_time} to {end_time}", room_id=room_id)
            # summary_thread_id = response.json()['message']['_id']

            # response = rocket.chat_post_message(summary, room_id=room_id, tmid=summary_thread_id, tmshow=False)
            
            # print("Done Room: " + curr_room.name + "\n=====")

def get_creds():
    userid = os.environ.get('ROCKETCHAT_PAT_USERID')
    token = os.environ.get('ROCKETCHAT_PAT_TOKEN')
    if userid is None or token is None:
        raise Exception("ROCKETCHAT_PAT_USERID and ROCKETCHAT_PAT_TOKEN must be set in environment")
    
    gemini_api_key = os.environ.get('GEMINI_API_KEY')
    if gemini_api_key is None:
        raise Exception("GEMINI_API_KEY must be set in environment")
    
    return userid, token, gemini_api_key

if __name__ == "__main__":
    main()
