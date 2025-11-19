import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

#load api key
load_dotenv()
api_key = os.getenv("api_key")

#connect to youtube's api
youtube = build("youtube", "v3", developerKey=api_key)

#get playlist
playlist_request = youtube.channels().list(
    part = "contentDetails",
    forUsername="ufc"
)
playlist_response = playlist_request.execute()
uploads_playlist_id = playlist_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


#get videos from the playlist
videos = []
next_page_token = None

print("⏳ Fetching UFC videos...")

while True:
    playlist_items_request = youtube.playlistItems().list(
        part = "snippet,contentDetails",
        playlistId = uploads_playlist_id,
        maxResults = 50,
        pageToken = next_page_token
    )
    playlist_items_response = playlist_items_request.execute()

    for item in playlist_items_response["items"]:
        videos.append({
            "video_id": item["contentDetails"]["videoId"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "published_at": item["contentDetails"]["videoPublishedAt"]
        })

    next_page_token = playlist_items_response.get("nextPageToken")
    if not next_page_token or len(videos) >= 1000:  # fetch up to 1000 videos 
        break

#get video stats 
video_ids = [v["video_id"] for v in videos]
stats = []
for i in range(0, len(video_ids), 50):
    chunk = video_ids[i:i+50]
    stats_request = youtube.videos().list(
        part="statistics",
        id=",".join(chunk)
    )
    stats_response = stats_request.execute()

    for item in stats_response["items"]:
        s = item["statistics"]
        stats.append({
            "video_id": item["id"],
            "views": int(s.get("viewCount", 0)),
            "likes": int(s.get("likeCount", 0)),
            "comments": int(s.get("commentCount", 0))
        })

#consolidate info + stats into a DataFrame
videos_df = pd.DataFrame(videos)
stats_df = pd.DataFrame(stats)
consolidate = videos_df.merge(stats_df, on="video_id", how="left")

#save to CSV to be organized
os.makedirs(r"C:\Users\shawa\Youtube_Api_Python\data\raw", exist_ok=True)
consolidate.to_csv(
    r"C:\Users\shawa\Youtube_Api_Python\data\raw\ufc_videos_raw.csv",
    index=False,
    encoding="utf-8"
)


print(f"Saved {len(consolidate)} UFC videos to C:\\Users\\shawa\\Youtube_Api_Python\\data\\raw\\ufc_videos_raw.csv")



