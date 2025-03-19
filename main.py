import os
from datetime import datetime
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

START_DATE = datetime(2025, 2, 16) 

def get_day_count():
    """Calculate how many days have passed since initial date."""
    today = datetime.today()
    delta = (today - START_DATE).days
    return delta + 1 

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
        counter = get_day_count()

        video_path = "reel.mp4"
        thumb = "reel.mp4.jpg"
        caption = f"Day {counter} #fy #foryou #owl #sound #daily #hoooo #soup #guy #porraeessa"

        # Post the video as Reel
        cl.clip_upload(video_path, caption, thumb)
        
        print(f"Reel successfully posted! {caption}")
        
    except Exception as e:
        print(f"Error to post reel: {e}")

# Using cron in workflow
post_reel()