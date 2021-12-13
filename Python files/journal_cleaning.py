import os

# voir les contributions sélections ajouter aux favoris partage partager sur facebook envoyer par e mail partager sur whatsapp plus d options
# delete above line from each journal, last thing left to clean

line = r"voir les contributions sélections ajouter aux favoris partage partager sur facebook envoyer par e mail partager sur whatsapp plus d options"
line2 = r"le monde avec afp contribuer sélections ajouter aux favoris partage partager sur facebook envoyer par e mail partager sur messenger plus d options"

for yr in range(1960, 2019):
    file_name = str(yr)
    file_name += '.txt'
    if 1960 <= yr <= 1969:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1960s\Journals", file_name)
        file = open(file_path, 'r+', encoding='utf-8')
        file = file.read()
        if line in file:
            file.replace(line, '')
        if line2 in file:
            file.replace(line2, '')
    if 1970 <= yr <= 1979:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1970s\Journals", file_name)
        file = open(file_path, 'r+', encoding='utf-8')
        file = file.read()
        if line in file:
            file.replace(line, '')
        if line2 in file:
            file.replace(line2, '')

    if 1980 <= yr <= 1980:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1980s\Journals", file_name)
        file = open(file_path, 'r+', encoding='utf-8')
        file = file.read()
        if line in file:
            file.replace(line, '')
        if line2 in file:
            file.replace(line2, '')
    if 1990 <= yr <= 1999:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1990s\Journals", file_name)
        file = open(file_path, 'r+', encoding='utf-8')
        file = file.read()
        if line in file:
            file.replace(line, '')
        if line2 in file:
            file.replace(line2, '')
    if 2000 <= yr <= 2009:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\2000s\Journals", file_name)
        file = open(file_path, 'r+', encoding='utf-8')
        file = file.read()
        if line in file:
            file.replace(line, '')
        if line2 in file:
            file.replace(line2, '')
    if 2010 <= yr <= 2019:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\2010s\Journals", file_name)
        file = open(file_path, 'r+', encoding='utf-8')
        file = file.read()
        if line in file:
            file.replace(line, '')
        if line2 in file:
            file.replace(line2, '')
