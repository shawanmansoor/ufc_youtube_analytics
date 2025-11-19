import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# load your .env file
load_dotenv()

# get API key from .env
api_key = os.getenv("api_key")

if not api_key:
    print("❌ Could not find your API key. Check .env file name or spelling.")
else:
    print("✅ API key loaded successfully!")

# connect to the YouTube API
youtube = build("youtube", "v3", developerKey=api_key)

# make a simple request: get UFC channel details
request = youtube.channels().list(
    part="snippet,statistics",
    forUsername="ufc"  # Official UFC channel ID
)

response = request.execute()

# print just the channel name and subscriber count
channel = response["items"][0]
name = channel["snippet"]["title"]
subs = channel["statistics"]["subscriberCount"]

print(f"✅ Connected successfully to YouTube API!")
print(f"Channel: {name}")
print(f"Subscribers: {subs}")
