import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Spotify Tracks Analytics",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Spotify Tracks Analytics Dashboard")
st.write("Interactive dashboard for exploring Spotify tracks, artists, genres and audio features.")

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("spotify.csv")
    return df

df = load_data()

# Remove missing values and convert columns to proper types
df["artists"] = df["artists"].fillna("Unknown").astype(str)
df["track_genre"] = df["track_genre"].fillna("Unknown").astype(str)
df["track_name"] = df["track_name"].fillna("Unknown").astype(str)

# Convert numeric columns
numeric_cols = [
    "popularity", "duration_ms", "danceability", "energy",
    "key", "speechiness", "acousticness", "instrumentalness",
    "liveness", "valence", "tempo"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=numeric_cols)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

artist = st.sidebar.multiselect(
    "Select Artist",
    sorted(df["artists"].dropna().astype(str).unique())
)

genre = st.sidebar.multiselect(
    "Select Genre",
    sorted(df["track_genre"].unique())
)

explicit = st.sidebar.multiselect(
    "Explicit",
    sorted(df["explicit"].unique())
)

filtered = df.copy()

if artist:
    filtered = filtered[filtered["artists"].isin(artist)]

if genre:
    filtered = filtered[filtered["track_genre"].isin(genre)]

if explicit:
    filtered = filtered[filtered["explicit"].isin(explicit)]

if filtered.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# -----------------------------
# KPI Cards
# -----------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("🎵 Total Songs", len(filtered))
c2.metric("🎤 Artists", filtered["artists"].nunique())
c3.metric("🎼 Genres", filtered["track_genre"].nunique())
c4.metric("⭐ Avg Popularity", round(filtered["popularity"].mean(), 1))

st.markdown("---")

# -----------------------------
# Chart 1
# -----------------------------
artist_pop = (
    filtered.groupby("artists")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    artist_pop,
    x="popularity",
    y="artists",
    orientation="h",
    color="popularity",
    title="Top 10 Artists by Average Popularity"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Chart 2
# -----------------------------
top_genres = (
    filtered.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .index
)

fig2 = px.box(
    filtered[filtered["track_genre"].isin(top_genres)],
    x="track_genre",
    y="popularity",
    color="track_genre",
    title="Popularity Distribution of Top Genres"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Chart 3
# -----------------------------
key_pop = (
    filtered.groupby("key")["popularity"]
    .mean()
    .reset_index()
)

fig3 = px.line(
    key_pop,
    x="key",
    y="popularity",
    markers=True,
    title="Average Popularity by Musical Key"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Chart 4
# -----------------------------
fig4 = px.scatter(
    filtered,
    x="danceability",
    y="energy",
    color="popularity",
    hover_data=["track_name", "artists"],
    title="Danceability vs Energy"
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# Chart 5
# -----------------------------
fig5 = px.box(
    filtered,
    x="explicit",
    y="popularity",
    color="explicit",
    title="Popularity of Explicit vs Non-Explicit Songs"
)

st.plotly_chart(fig5, use_container_width=True)

import plotly.graph_objects as go

# -----------------------------
# Chart 6 - Song Duration Distribution
# -----------------------------
fig6 = px.histogram(
    filtered,
    x="duration_ms",
    nbins=30,
    title="Distribution of Song Duration",
    color_discrete_sequence=["teal"]
)

st.plotly_chart(fig6, use_container_width=True)

# -----------------------------
# Chart 7 - Genre Treemap
# -----------------------------
genre_count = (
    filtered["track_genre"]
    .value_counts()
    .reset_index()
)

genre_count.columns = ["Genre", "Songs"]

fig7 = px.treemap(
    genre_count,
    path=["Genre"],
    values="Songs",
    color="Songs",
    title="Songs by Genre"
)

st.plotly_chart(fig7, use_container_width=True)

# -----------------------------
# Chart 8 - Correlation Heatmap
# -----------------------------
corr = filtered[
    [
        "popularity",
        "danceability",
        "energy",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo"
    ]
].corr()

fig8 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation of Audio Features"
)

st.plotly_chart(fig8, use_container_width=True)

# -----------------------------
# Chart 9 - Musical Key Distribution
# -----------------------------
key_count = (
    filtered["key"]
    .value_counts()
    .reset_index()
)

key_count.columns = ["Key", "Songs"]

fig9 = px.pie(
    key_count,
    names="Key",
    values="Songs",
    hole=0.4,
    title="Distribution of Musical Keys"
)

st.plotly_chart(fig9, use_container_width=True)

# -----------------------------
# Chart 10 - Genre to Artist Sunburst
# -----------------------------
top_genres = (
    filtered["track_genre"]
    .value_counts()
    .head(10)
    .index
)

sunburst_df = filtered[
    filtered["track_genre"].isin(top_genres)
]

fig10 = px.sunburst(
    sunburst_df,
    path=["track_genre", "artists"],
    title="Genre → Artist Distribution"
)

st.plotly_chart(fig10, use_container_width=True)

# -----------------------------
# Show Dataset
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(filtered.head(20))

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    """
    **Spotify Tracks Analytics Dashboard**

    Developed using **Python, Pandas, Plotly and Streamlit**

    **Author:** Dheeraj dabbeti 
    """
)