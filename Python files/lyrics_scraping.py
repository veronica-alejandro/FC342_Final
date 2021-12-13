import lyricsgenius
import os

genius = lyricsgenius.Genius('')  # API key left blank for privacy

file = open('songs.txt', 'r', encoding = 'utf-8')

def lyrics_to_file(data):
    song = genius.search_song(data[0], data[1])
    lyrics = song.lyrics
    year = int(data[2])
    file_name = str(year)
    if 1980 <= year <= 1989:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1980s\Songs", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(lyrics)
    elif 1990 <= year <= 1999:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1990s\Songs", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(lyrics)
    elif 2000 <= year <= 2009:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\2000s\Songs", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(lyrics)
    elif 2010 <= year <= 2019:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\2010s\Songs", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(lyrics)


for song in file.readlines():
    song_data = song.strip()
    song_data = song_data.split('/')
    lyrics_to_file(song_data)

file.close()
