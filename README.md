# 🥊 UFC YouTube Analytics Dashboard


## 📘 Overview
This is a passion project of mine which analyzes UFC's official Youtube channel to uncover engagement trends across different content types — including press conferences, weigh-ins, faceoffs, interviews, full fights, and embedded series. The analysis focuses on identifying what types of content generate the most audience interaction/engagement (likes, comments, and views), including with a special case study on Alex Pereira (“Poatan”), one of the UFC’s — if not the most — popular athlete today.

## 🎯 Objectives
1) Clean and structure YouTube API data into an "analyzable" form.

2) Categorize videos by content type using text classifications.

3) Compute engagement metrics to compare performances between content types.

4) Evaluate Alex Pereira’s engagement compared to UFC averages.

5) Visualize trends and performance insights with Power BI.

## ⚙️ Tech Stack

| **Category** | **Tool / Library** | **Purpose** |
|:-------------|:------------------:|-------------:|
| **Data Collection** | 🧩 YouTube Data API v3 | Fetches video metadata, performance metrics (views, likes, comments, publish date) |
| **Data Processing** | 🐍 Python (Pandas, NumPy) | Cleans raw data, fixes encoding, and categorizes videos by content type |
| **Data Storage** | 📁 CSV / TXT Files | Stores cleaned and summarized datasets for Power BI visualization |
| **Visualization** | 📊 Microsoft Power BI | Builds interactive dashboards for engagement and performance trends |

## 📊 Key Metrics
**Engagement Rate (%)** = (Likes + Comments) ÷ Views × 100

## 📈 Dashboard Highlights
**Bar Chart:** Average engagement across content types

**KPI Cards:** Compares overall average engagement to Pereira's average engagement

**Scatter Plot:** Views vs Engagement Rate for videos

**Trend Line:** Shows correlation between reach and engagement

## 🧠 Findings

Press Conferences and Weigh-Ins drive the most engagement overall.

Alex Pereira’s videos outperform the channel average by ~20%.

Interviews featuring Pereira have the highest engagement-per-viewer.

Full fights draw high reach but comparatively lower engagement.

## 🧩 Future Improvements

1) Automate daily YouTube API pulls via a scheduled script, so the data stays up to date

2) Add deep analysis for YouTube comments, seeing how many times a phrase/fighter was brought up, seeing if comments are negative/positive, etc.

3) Expand comparison across multiple fighters or events

Deploy Power BI report to a public dashboard (Power BI Service).



