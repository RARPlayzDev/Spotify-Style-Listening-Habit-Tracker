import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("listening_history.csv")

# -------------------------------
# 1. Display Listening History
# -------------------------------
print("\nListening History (Preview):")
print(data.head(15).to_string(index=False))

# ----------------------------------
# 2. Total Plays Per Artist
# ----------------------------------
artist_play_count = (
    data.groupby("Artist")["Times_Played"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Plays Per Artist:")
print(artist_play_count.to_string())

# ----------------------------------
# 3. Top 5 Most Played Songs
# ----------------------------------
top_songs = (
    data.sort_values(by="Times_Played", ascending=False)
    .head(5)[["Song", "Artist", "Times_Played"]]
)

print("\nTop 5 Most Played Songs:")
print(top_songs.to_string(index=False))

# ----------------------------------
# 4. Pie Chart: Artist Distribution
# ----------------------------------
plt.figure(figsize=(8, 8))
artist_play_count.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Total Listening Share by Artist", fontsize=14)
plt.ylabel("")
plt.tight_layout()
plt.show()

# ----------------------------------
# 5. Bar Chart: Top 5 Songs
# ----------------------------------
plt.figure(figsize=(10, 5))
plt.bar(top_songs["Song"], top_songs["Times_Played"])
plt.title("Top 5 Most Played Songs", fontsize=14)
plt.xlabel("Song")
plt.ylabel("Times Played")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
