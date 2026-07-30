# 🎵 Spotify Tracks Analytics Dashboard

## 📌 Project Overview

This project analyzes the Spotify Tracks Dataset using Python, Pandas, Plotly, and Streamlit. The objective is to explore song popularity, artists, genres, and audio features through data cleaning, exploratory data analysis (EDA), interactive visualizations, and a Streamlit dashboard.

##Live Dashboard
https://lusngjjmotb5gokehhjdku.streamlit.app/

---

## 📂 Dataset

- **Dataset:** Spotify Tracks Dataset
- **Source:** Kaggle
- **Records:** 114,000 songs
- **Features:** 20 columns

The dataset contains information about:
- Track Name
- Artist
- Album Name
- Genre
- Popularity
- Duration
- Danceability
- Energy
- Tempo
- Acousticness
- Speechiness
- Instrumentalness
- Liveness
- Valence
- Musical Key
- Explicit Content

---

## 🎯 Project Objectives

- Clean and preprocess the Spotify dataset.
- Perform Exploratory Data Analysis (EDA).
- Identify trends in song popularity.
- Compare genres and artists.
- Analyze relationships between audio features.
- Build an interactive Streamlit dashboard.

---

## 📊 Visualizations

The project includes the following interactive visualizations:

1. Top 10 Artists by Average Popularity
2. Genre Popularity Distribution
3. Average Popularity by Musical Key
4. Danceability vs Energy
5. Explicit vs Non-Explicit Song Popularity
6. Distribution of Song Duration
7. Number of Songs by Genre (Treemap)
8. Correlation Heatmap of Audio Features
9. Distribution of Musical Keys
10. Genre → Artist Sunburst Chart

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit

---

## 📁 Project Structure

```
Spotify_Analytics/
│── app.py
│── spotify.csv
│── notebook.ipynb
│── requirements.txt
│── README.md
```

---

## ▶️ Running the Project

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📈 Key Findings

- Some artists consistently achieve higher average popularity than others.
- Music genres differ significantly in popularity.
- Danceability and energy show a positive relationship.
- Explicit and non-explicit songs have different popularity distributions.
- Most songs fall within a common duration range.
- Certain genres contain a much larger number of songs.
- Audio features exhibit both positive and negative correlations.
- Musical keys vary in frequency across songs.
- The sunburst chart highlights the relationship between genres and artists.

---

## ✅ Conclusion

This project demonstrates how Python, Pandas, Plotly, and Streamlit can be used to analyze and visualize Spotify music data. The interactive dashboard allows users to explore artists, genres, popularity, and audio features, making it easier to identify patterns and gain meaningful insights from the dataset.

---

## 👩‍🎓 Author

**Dheeraj Dabbeti**

MS in Data Science

University of Europe for Applied Sciences

---

## 📚 References

- Spotify Tracks Dataset – Kaggle
- Python Documentation
- Pandas Documentation
- Plotly Documentation
- Streamlit Documentation
