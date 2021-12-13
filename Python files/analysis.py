import pandas as pd
import matplotlib.pyplot as plt
import os

journal_counts = [0] * 6
journal_yrs = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']
journal_dict = dict(zip(journal_yrs, journal_counts))

song_yrs = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']
song_counts = [0] * 6
song_dict = dict(zip(song_yrs, song_counts))

file_ang = open(r"G:\My Drive\Fall2021\FC 342\Final project\anglicisms.txt", 'r+', encoding='utf-8')
file_ang = file_ang.read()
anglicisms = file_ang.split('\n')
anglicisms.pop(anglicisms.index(anglicisms[-1]))


# next step is to look at each cleaned article/song looking for anglicisms
# add up the counts for each decade to the dictionary

def journal_counts():
    years = list(range(1960, 2020))
    for yr in years:
        if 1960 <= yr <= 1969:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\1960s\Journals"
            yr_file = str(yr) + '.txt'
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            journal_dict['1960s'] += count
        elif 1970 <= yr <= 1979:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\1970s\Journals"
            yr_file = str(yr) + '.txt'
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            journal_dict['1970s'] += count
        elif 1980 <= yr <= 1989:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\1980s\Journals"
            yr_file = str(yr) + '.txt'
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            journal_dict['1980s'] += count
        elif 1990 <= yr <= 1999:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\1990s\Journals"
            yr_file = str(yr) + '.txt'
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            journal_dict['1990s'] += count
        elif 2000 <= yr <= 2009:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\2000s\Journals"
            yr_file = str(yr) + '.txt'
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            journal_dict['2000s'] += count
        elif 2010 <= yr <= 2019:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\2010s\Journals"
            yr_file = str(yr) + '.txt'
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            journal_dict['2010s'] += count


def song_counts():
    years = list(range(1985, 2020))
    years.pop(4)
    for yr in years:
        if 1985 <= yr <= 1989:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\1980s\Songs"
            yr_file = str(yr)
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            song_dict['1980s'] += count
        if 1990 <= yr <= 1999:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\1990s\Songs"
            yr_file = str(yr)
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            song_dict['1990s'] += count
        if 2000 <= yr <= 2009:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\2000s\Songs"
            yr_file = str(yr)
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            song_dict['2000s'] += count
        if 2010 <= yr <= 2019:
            count = 0
            words = []
            dir = r"G:\My Drive\Fall2021\FC 342\Final project\2010s\Songs"
            yr_file = str(yr)
            file_path = os.path.join(dir, yr_file)
            file = open(file_path, 'r', encoding='utf-8')
            file = file.read()
            file = file.split()
            for word in anglicisms:
                if word in file:
                    count += 1
                    words.append(word)
            song_dict['2010s'] += count


journal_counts()
song_counts()

journal_keys = list(journal_dict.keys())
journal_values = list(journal_dict.values())

song_keys = list(song_dict.keys())
song_values = list(song_dict.values())


df_journal = pd.DataFrame({'Decade': journal_keys, 'Journals': journal_values})
df_songs = pd.DataFrame({'Decade': song_keys, 'Songs': song_values})
df_paired = pd.merge(df_journal, df_songs, on = 'Decade')
df_paired.plot.bar(x='Decade', color = ['sandybrown', 'saddlebrown'])
plt.xlabel('Decade')
plt.ylabel('Anglicism count')

df_journal.plot.bar(x = 'Decade', color = 'sandybrown')
plt.xlabel('Decade')
plt.ylabel('Anglicism count')

df_songs.plot.bar(x = 'Decade', color = 'saddlebrown')
plt.xlabel('Decade')
plt.ylabel('Anglicism count')
plt.show()