🥊 UFC YouTube Analytics Dashboard
📘 Overview

This project analyzes UFC’s official YouTube channel to uncover engagement trends across different content types — including press conferences, weigh-ins, faceoffs, interviews, full fights, and embedded series.

The analysis focuses on identifying what types of content generate the most audience interaction (likes, comments, and views), with a special case study on Alex Pereira (“Poatan”) — one of the UFC’s most popular athletes.

🎯 Objectives

Clean and structure YouTube API data into analyzable form.

Categorize videos by content type using text classification.

Compute engagement metrics to compare performance.

Visualize trends and performance insights in Power BI.

Evaluate Alex Pereira’s engagement compared to UFC averages.

⚙️ Tech Stack
Tool	Purpose
Python (Pandas, NumPy, Regex)	Data cleaning, feature engineering
YouTube Data API v3	Data collection (video stats & metadata)
Power BI	Dashboard creation & visualization
CSV / TXT Outputs	Intermediate storage & reporting
📊 Key Metrics

Engagement Rate (%)

Engagement Rate
=
Likes + Comments
Views
×
100
Engagement Rate=
Views
Likes + Comments
	​

×100

This allows comparison of audience interaction across videos of vastly different view counts.

📂 Project Structure
Youtube_Api_Python/
│
├── data/
│   ├── raw/                      # Original API pulls
│   ├── clean/                    # Cleaned datasets for Power BI
│   │   ├── ufc_videos_clean.csv
│   │   ├── content_type_summary.csv
│   │   └── analysis_summary.txt
│
├── scripts/
│   ├── data_cleaning.py          # Cleans & filters data
│   ├── categorize_videos.py      # Classifies videos into content types
│   └── summarize_engagement.py   # Calculates averages & exports results
│
├── dashboard/
│   └── ufc_engagement.pbix       # Power BI dashboard file
│
└── README.md                     # Project documentation

📈 Dashboard Highlights

Bar Chart: Average engagement by content type

KPI Cards:

Overall average engagement

Alex Pereira (all videos)

Alex Pereira (interviews only)

Scatter Plot: Views vs Engagement Rate (each dot = video)

Trend Line: Shows correlation between reach and engagement

Slicer Filters: Quickly isolate Pereira or specific video types

🧠 Insights

Press Conferences and Weigh-Ins drive the most engagement overall.

Alex Pereira’s videos outperform the channel average by ~20%.

Interviews featuring Pereira have the highest engagement-per-viewer.

Full fights draw high reach but comparatively lower engagement.

🧩 Future Improvements

Automate daily YouTube API pulls via a scheduled script.

Add sentiment analysis for YouTube comments.

Expand comparison across multiple fighters or events.

Deploy Power BI report to a public dashboard (Power BI Service).

💬 Example Output
📊 Average Engagement by Content Type (excluding 'Other'):
Press Conference     1.89%
Weigh-In             1.80%
Embedded Series      1.70%
Interview            1.67%
Full Fight           1.28%
Faceoff              1.05%

🔥 Alex Pereira Engagement Comparison:
Overall Avg: 1.85%
Alex Pereira (all videos): 2.22%
Alex Pereira Interviews: 2.74%
