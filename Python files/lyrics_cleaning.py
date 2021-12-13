import regex as re
import os

annees = list(range(1985, 2020))
annees.pop(4)


def clean_lyrics(inp):
    print('Cleaning lyrics...')
    inp = inp.lower()
    extra = ['embed', 'share', 'url', 'copy']
    for word in extra:
        if word in inp:
            inp = inp.replace(word, '')
    nums = r'[0-9]'
    text = re.sub(nums, '', inp)
    pattern = r'\[[^\]]*\]'  # regex by Can Berk Güder on stack overflow //
    # https://stackoverflow.com/questions/640001/how-can-i-remove-text-within-parentheses-with-a-regex/40621332
    text = re.sub(pattern, '', text)
    ptrn = r"[^a-zA-ZÀÁÄàáäÉÈËÊéèëêÙùÜüçÇ']"
    text = re.sub(ptrn, ' ', text)
    text = re.sub(' +', ' ', text)
    text = text.strip()

    return text


for yr in annees:
    if 1985 <= yr <= 1989:
        dir = r"G:\My Drive\Fall2021\FC 342\Final project\1980s\Songs"
        print('Cleaning song from {}...'.format(yr))

        file_path = os.path.join(dir, str(yr))
        file = open(file_path, 'r', encoding='utf-8')
        file_r = file.read()

        txt = clean_lyrics(file_r)
        file.close()

        file = open(file_path, 'w', encoding='utf-8')
        file.write(txt)
    elif 1990 <= yr <= 1999:
        dir = r"G:\My Drive\Fall2021\FC 342\Final project\1990s\Songs"
        print('Cleaning song from {}...'.format(yr))

        file_path = os.path.join(dir, str(yr))
        file = open(file_path, 'r', encoding='utf-8')
        file_r = file.read()

        txt = clean_lyrics(file_r)
        file.close()

        file = open(file_path, 'w', encoding='utf-8')
        file.write(txt)
    elif 2000 <= yr <= 2009:
        dir = r"G:\My Drive\Fall2021\FC 342\Final project\2000s\Songs"
        print('Cleaning song from {}...'.format(yr))

        file_path = os.path.join(dir, str(yr))
        file = open(file_path, 'r', encoding='utf-8')
        file_r = file.read()

        txt = clean_lyrics(file_r)
        file.close()

        file = open(file_path, 'w', encoding='utf-8')
        file.write(txt)
    elif 2010 <= yr <= 2019:
        dir = r"G:\My Drive\Fall2021\FC 342\Final project\2010s\Songs"
        print('Cleaning song from {}...'.format(yr))

        file_path = os.path.join(dir, str(yr))
        file = open(file_path, 'r', encoding='utf-8')
        file_r = file.read()

        txt = clean_lyrics(file_r)
        file.close()

        file = open(file_path, 'w', encoding='utf-8')
        file.write(txt)
