import pandas as pd

# file paths
clean_path = r"C:\Users\shawa\Youtube_Api_Python\data\clean\ufc_videos_clean.csv"
csv_output = r"C:\Users\shawa\Youtube_Api_Python\data\clean\content_type_summary.csv"
pereira_output = r"C:\Users\shawa\Youtube_Api_Python\data\clean\pereira_summary.csv"

# load clean data
df = pd.read_csv(clean_path, encoding="utf-8-sig")

# exclude "other" content types
filtered = df[df["content_type"] != "Other"].copy()

# calculate and group average engagement by content type
avg_engagement = (
    filtered.groupby("content_type")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
    * 100
).round(2)

# convert to dataframe 
summary = (
    avg_engagement
    .reset_index()
    .rename(columns={"engagement_rate": "engagement_rate_%"})
)
summary.to_csv(csv_output, index=False, encoding="utf-8-sig")

# pereira comparison
pereira = df[df["is_pereira"]].copy()
overall_avg = (df["engagement_rate"].mean() * 100).round(2)
pereira_all = (pereira["engagement_rate"].mean() * 100).round(2)
pereira_interviews = (
    pereira[pereira["content_type"] == "Interview"]["engagement_rate"].mean() * 100
).round(2)

# save summary
pereira_summary = pd.DataFrame([{
    "Overall_Avg_%": overall_avg,
    "Pereira_All_Videos_%": pereira_all,
    "Pereira_Interviews_%": pereira_interviews
}])
pereira_summary.to_csv(pereira_output, index=False, encoding="utf-8-sig")


