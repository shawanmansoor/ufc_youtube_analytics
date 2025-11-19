import os
import re
import pandas as pd

# file paths
raw_path = r"C:\Users\shawa\Youtube_Api_Python\data\raw\ufc_videos_raw.csv"
clean_path = r"C:\Users\shawa\Youtube_Api_Python\data\clean\ufc_videos_clean.csv"

# load data/check if there is a path
if not os.path.exists(raw_path):
    raise FileNotFoundError(f"Could not find raw CSV at: {raw_path}")

df = pd.read_csv(raw_path, encoding="utf-8-sig")

# keep only columns that are necessary
df = df[["video_id", "title", "description", "published_at", "views", "likes", "comments"]].copy()

# clean data types
df["title"] = df["title"].fillna("").astype(str)
df["description"] = df["description"].fillna("").astype(str)
df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce").dt.date

for col in ["views", "likes", "comments"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# engagement rate calculation and cleaning for broken data
df["engagement_rate"] = (df["likes"] + df["comments"]) / df["views"].replace(0, pd.NA)
df["engagement_rate"] = df["engagement_rate"].fillna(0)

# video type classifications
CONTENT_RULES = {
    "Press Conference": ["press conference", "post-fight press", "post fight press"],
    "Weigh-In": ["weigh-in", "weigh in"],
    "Faceoff": ["faceoff", "face-off", "staredown", "stare down"],
    "Full Fight": ["free fight", "full fight"],
    "Interview": ["interview", "post-fight interview", "post fight interview"],
    "Embedded Series": ["embedded", "countdown"]
}

def classify_content(title_desc):
    text = f"{title_desc}".lower()
    for label, keywords in CONTENT_RULES.items():
        if any(k in text for k in keywords):
            return label
    return "Other"

df["content_type"] = (df["title"] + " " + df["description"]).apply(classify_content)

# detect alex pereira
df["is_pereira"] = (
    df["title"].str.contains(r"\b(alex\s+pereira|poatan|chama)\b", case=False, na=False) |
    df["description"].str.contains(r"\b(alex\s+pereira|poatan|chama)\b", case=False, na=False)
)

# keep only relevant columns
df = df[["video_id", "title", "description", "views", "likes", "comments", "engagement_rate", "published_at", "content_type", "is_pereira"]]

# Save clean file
os.makedirs(os.path.dirname(clean_path), exist_ok=True)
df.to_csv(clean_path, index=False, encoding="utf-8")

print(f"Clean dataset saved: {clean_path}")
print(f"Total videos: {len(df):,}")
print("Columns:", ", ".join(df.columns))