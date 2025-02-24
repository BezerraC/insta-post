import os
import schedule
import time
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
        counter = 9
    return counter

def save_counter(counter):
    with open("counter.txt", "w") as f:
        f.write(str(counter))

# Auth in Instagram
def login():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
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

# Schedule the post every days at 5pm
schedule.every().day.at("17:00").do(post_reel)

print("Initialize bot! Wait the time to post...")

# Keep script runing
while True:
    schedule.run_pending()
    time.sleep(10)
