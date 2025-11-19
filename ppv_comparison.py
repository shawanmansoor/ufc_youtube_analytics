import pandas as pd

# Load cleaned videos file
df = pd.read_csv(
    r"C:\Users\shawa\Youtube_Api_Python\data\clean\ufc_videos_clean.csv",
    encoding="utf-8-sig"
)

# 1) Detect UFC ### pattern
pattern = r'(?i)\b#?ufc\s*([0-9]{3})\b'
df["ppv_num"] = df["title"].str.extract(pattern, expand=False)

# 2) Normalize event tags like "UFC 320"
df["event_tag"] = df["ppv_num"].dropna().astype(int).map(lambda n: f"UFC {n}")
df.loc[df["ppv_num"].isna(), "event_tag"] = pd.NA

# 3) Build grouped PPV table
ppv = df.dropna(subset=["event_tag"]).copy()

ppv_summary = (
    ppv.groupby("event_tag")
       .agg(
           count_videos=("video_id", "count"),
           sum_views=("views", "sum"),
           avg_engagement_rate=("engagement_rate", "mean"),
           median_engagement_rate=("engagement_rate", "median"),
           avg_likes=("likes", "mean"),
           avg_comments=("comments", "mean"),
       )
       .reset_index()
)

# 🔥 4) FILTER: Keep only events with more than 5 videos
ppv_summary_filtered = ppv_summary[ppv_summary["count_videos"] > 5]

# Get list of events that passed the filter
valid_events = ppv_summary_filtered["event_tag"].tolist()

print("Events with more than 5 videos:", valid_events)

# 5) Save everything to an Excel workbook
excel_path = r"C:\Users\shawa\Youtube_Api_Python\data\clean\ppv_events.xlsx"

with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
    # Summary sheet (already filtered)
    ppv_summary_filtered.to_excel(writer, sheet_name="PPV_Summary", index=False)

    # Sheets per event (only events with >5 videos)
    for event in valid_events:
        subset = ppv[ppv["event_tag"] == event]
        sheet_name = event.replace(" ", "_")[:31]  # safe sheet name
        subset.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"📄 Saved Excel with filtered events (>5 videos):\n{excel_path}")
