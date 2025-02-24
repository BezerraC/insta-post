import os
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

# Read and add counter
def get_counter():
    try:
        with open("counter.txt", "r") as f:
            counter = int(f.read())
    except FileNotFoundError:
        counter = 10
    return counter

def save_counter(counter):
    with open("counter.txt", "w") as f:
        f.write(str(counter))

# Auth in Instagram
def login():
    cl = Client()
    session_file = "session.json"

    if os.path.exists(session_file):
        cl.load_settings(session_file)
    else:
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(session_file)

    return cl

# Function to post a Reel
def post_reel():
    try:
        print("Posting Reel...")
        cl = login()

        # Get the counter of the day
        counter = get_counter()

        video_path = "reel.mp4"
        thumb = "reel.mp4.jpg"
        caption = f"Day {counter} #fy #foryou #owl #sound #daily #hoooo #soup #guy #porraeessa"

        # Post the video as Reel
        cl.clip_upload(video_path, caption, thumb)
        
        print(f"Reel successfully posted! {caption}")

        # Update the counter file
        save_counter(counter + 1)
        
    except Exception as e:
        print(f"Error to post reel: {e}")

# Using cron in workflow
post_reel()