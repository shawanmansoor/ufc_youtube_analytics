# 🥊 UFC YouTube Analytics Dashboard


## 📘 Overview
This is a passion project of mine which analyzes UFC's official Youtube channel to uncover engagement trends across different content types — including press conferences, weigh-ins, faceoffs, interviews, full fights, and embedded series. The analysis focuses on identifying what types of content generate the most audience interaction/engagement (likes, comments, and views), including with a special case study on Alex Pereira (“Poatan”), one of the UFC’s — if not the most — popular athlete today.

## 🎯 Objectives
1) Clean and structure YouTube API data into an "analyzable" form.

2) Categorize videos by content type using text classifications.

3) Compute engagement metrics to compare performances and tendencies between content types.

4) Evaluate Alex Pereira’s engagement compared to UFC averages.

5) Compare engagement between the largest Pay-Per-View events.

6) Visualize trends and performance insights with Power BI.

## ⚙️ Tech Stack

| **Category** | **Tool / Library** | **Purpose** |
|:-------------|:------------------:|-------------:|
| **Data Collection** | 🧩 YouTube Data API v3 | Fetches video metadata, performance metrics (views, likes, comments, publish date) |
| **Data Processing** | 🐍 Python (Pandas, NumPy) | Cleans raw data, fixes encoding, and categorizes videos by content type |
| **Data Storage** | 📁 CSV / TXT Files | Stores cleaned and summarized datasets for Power BI visualization |
| **Visualization** | 📊 Microsoft Power BI | Builds interactive dashboards for engagement and performance trends |

## 📊 Key Metric

Engagement Rate measures how actively viewers interact with a piece of content.

For this project, it represents the percentage of viewers who liked, commented, or otherwise engaged with a UFC video relative to its total views.
**Engagement Rate (%)** = (Likes + Comments) ÷ Views × 100

**What is Considered a Good/Bad Engagement Rate?**

Engagement benchmarks vary by platform, but on YouTube-style content:
- Low Engagement: < 1%
  - Content is reaching viewers but not driving meaningful interaction.
    
- Average Engagement: 1% – 2%
  - Most general creator content falls in this range.
    
- High Engagement: 2% – 5%+
  - Strong audience connection — typically seen in viral clips, big announcements, or highly emotional/controversial moments.
    
- Exceptional Engagement: 6%+
  - Rare. Indicates extremely compelling content and strong community interest.

## 📈 Dashboard Highlights

**📍 Dashboard 1 — YouTube Content Engagement Overview**

This dashboard analyzes 999 UFC YouTube videos across multiple content types to understand how fans interact with UFC media.

Key highlights:

- From the beginning of August to the end of Octobver, UFC's channel ammassed 226M total views, 4M likes, and 245K comments.

- The overall average engagement rate is 1.85%, which is strong for a large sports brand.

- Press Conferences, Weigh-Ins, Embedded Series, and Interviews are all over 1.5% average, suggesting fans respond strongly to behind-the-scenes or narrative-driven content.

- Scatter plot analysis shows no direct correlation between high views and high engagement — meaning viral videos don’t always drive meaningful interaction.

- Views and uploads are unevenly distributed across content types, helping identify where UFC focuses most of its content production and which audiences they are tailored to.

**📍 Dashboard 2 — Alex Pereira Pay-Per-View (PPV) Engagement Breakdown**

This dashboard zooms in on one fighter—Alex Pereira—to understand how his content performs across major UFC PPVs.

Key highlights:

- Pereira-related videos average 2.22% engagement, which is above the UFC channel-wide average at 1.85%.

- Pereira’s videos also average 848K views, showing significantly boosted reach especially during his PPV fight weeks.

- UFC 320 content delivered the strongest overall performance, achieving the highest median engagement rate, the most likes, and the largest number of uploads — highlighting how heavily the organization invested in promoting Pereira during this event.

Top-performing videos often include:

- Post-fight reactions

- Emotional or dramatic moments

  - Overall, engagement rate comparisons across PPVs show consistent interest regardless of the event, signaling a strong and loyal audience base.

## 🧠 Findings

**Content Types**

- Press Conferences are focused to audiences/fans who want to see the drama and tensions before and after the fights. The UFC sees this as a reliable way to spark conversation, engagement, and build up anticipation.

- Weigh-Ins are focused on viewers who enjoy the final faceoffs and the emotional pre-fight moment. Its strong engagement shows its virality is tied to last-minute intensity.

- Embedded Series are tailored to fans who enjoy seeing the BTS of fighters' preparations before the fights. These help deepen fan connections to fighters and the organization as well as strengthens narratives leading to events.

- Interviews are tailored to dedicated fans who want fighter insights and personalities. They are the most uploaded to build fighter brands and connections with fans.

- Full fights are for casual as well has hardcore fans. They generate big viewership but low interaction (people watch it more than comment). This is a perfect example of UFC's "evergreen" content.

- Faceoffs are tailored to fans who just want to see the quick hype moments. Although engagement is low, they do help promote rivalries.

**Pereira x PPV**

- Pereira is a high-engagement fighter, outperforming the platform’s average.

- PPV build-up content performs exceptionally well, especially when tied to dramatic or narrative moments.

- UFC’s audience rewards authenticity, emotion, and big fight moments, rather than just polished promotional content.

##🎯 Strategic Recommendations

The UFC is on top of their game when it comes to knowing who their audience is. However, here are some other suggestions I have.

**1) Partner with MMA & Combat Sports Content Creators.**
      - Youtubers and narrative-based MMA creators already havce:
          - Extremely loyal audiences
          - Emotional storytelling formats
          - High engagement per video
          - Deep knowledge of fighters and rivalries from a fan's POV.
          
**2) Incentivize "Fan Reaction Content"
      - Reactions, hype edits, and emotional responses have consistent high engagement.
      - UFC can spark this by:
        - Creating weekly "Best Content" features or reactions for each event.
        - Promote fan edits on social platforms.

**3) Fighter Personality Spotlights"**
Since interviews and Embedded content do great:
    - Create personality-driven series:
       - “5 Things You Didn’t Know About ___”
       - “A Day in the Life of ____”
       - “Fighter Origins: How They Started”

## 🧩 Future Improvements

1) **Automate daily YouTube API pulls** via a scheduled script, so the data stays up to date

2) Add **deep analysis for YouTube comments**, seeing how many times a phrase/fighter was brought up, seeing if comments are negative/positive, etc.

3) Compare other channels of UFC's top competitors (Boxing, other MMA organizations, etc.) 
