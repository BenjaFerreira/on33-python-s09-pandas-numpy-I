import pandas as pd

df = pd.read_csv("C:/Users/Usuario/OneDrive/Área de Trabalho/On33-Python/FORK/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv")

#print(df.head())
#print (df.columns)
print(df.dtypes)

to_parse = ['All Time Rank', 'Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'YouTube Views', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach', 'Deezer Playlist Reach', 'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']

for column in to_parse:
    df[column] = df[column].str.replace(",", "").astype(float)

print(df.dtypes)

df['Release Date'] = pd.to_datetime((df['Release Date']), format="mixed")
print(df.dtypes)

df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
print(df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts', 'Streaming Popularity']].head())

df['Total Streaming'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)
print(df['Total Streaming'].head())

filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streaming'] > 1_000_000)]
print(filtered_df.head())

df.to_json('./musicasMaisPopulares.json',
index=False)


