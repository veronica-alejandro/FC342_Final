from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
import regex as re
import os

annees = list(range(2019, 2020))

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


def get_random_article(first, yr):
    url = 'https://www.lemonde.fr/archives-du-monde/'
    browser.get(url)
    if first:
        button = browser.find_element(By.XPATH, '//*[@id="js-body"]/div[5]/div/footer/button[1]')
        button.click()
    time.sleep(0.5)

    mois = ['//*[@id="habillagepub"]/section[1]/section[2]/a[1]', '//*[@id="habillagepub"]/section[1]/section[2]/a[2]',
            '//*[@id="habillagepub"]/section[1]/section[2]/a[3]', '//*[@id="habillagepub"]/section[1]/section[2]/a[4]',
            '//*[@id="habillagepub"]/section[1]/section[2]/a[5]', '//*[@id="habillagepub"]/section[1]/section[2]/a[6]',
            '//*[@id="habillagepub"]/section[1]/section[2]/a[7]', '//*[@id="habillagepub"]/section[1]/section[2]/a[8]',
            '//*[@id="habillagepub"]/section[1]/section[2]/a[9]', '//*[@id="habillagepub"]/section[1]/section[2]/a[10]',
            '//*[@id="habillagepub"]/section[1]/section[2]/a[11]',
            '//*[@id="habillagepub"]/section[1]/section[2]/a[12]']

    jours = ['//*[@id="habillagepub"]/section[1]/section[3]/a[1]', '//*[@id="habillagepub"]/section[1]/section[3]/a[2]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[3]', '//*[@id="habillagepub"]/section[1]/section[3]/a[4]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[5]', '//*[@id="habillagepub"]/section[1]/section[3]/a[6]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[7]', '//*[@id="habillagepub"]/section[1]/section[3]/a[8]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[9]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[10]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[11]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[12]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[13]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[14]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[15]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[16]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[17]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[18]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[19]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[20]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[21]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[22]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[23]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[24]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[25]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[26]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[27]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[28]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[29]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[30]',
             '//*[@id="habillagepub"]/section[1]/section[3]/a[31]']

    mois_2017 = ['//*[@id="habillagepub"]/section[1]/section[3]/a[1]', '//*[@id="habillagepub"]/section[1]/section[3]/a[2]',
            '//*[@id="habillagepub"]/section[1]/section[3]/a[3]', '//*[@id="habillagepub"]/section[1]/section[3]/a[4]',
            '//*[@id="habillagepub"]/section[1]/section[3]/a[5]', '//*[@id="habillagepub"]/section[1]/section[3]/a[6]',
            '//*[@id="habillagepub"]/section[1]/section[3]/a[7]', '//*[@id="habillagepub"]/section[1]/section[3]/a[8]',
            '//*[@id="habillagepub"]/section[1]/section[3]/a[9]', '//*[@id="habillagepub"]/section[1]/section[3]/a[10]',
            '//*[@id="habillagepub"]/section[1]/section[3]/a[11]',
            '//*[@id="habillagepub"]/section[1]/section[3]/a[12]']

    jours_2017 = ['//*[@id="habillagepub"]/section[1]/section[4]/a[1]', '//*[@id="habillagepub"]/section[1]/section[4]/a[2]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[3]', '//*[@id="habillagepub"]/section[1]/section[4]/a[4]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[5]', '//*[@id="habillagepub"]/section[1]/section[4]/a[6]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[7]', '//*[@id="habillagepub"]/section[1]/section[4]/a[8]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[9]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[10]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[11]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[12]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[13]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[14]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[15]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[16]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[17]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[18]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[19]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[20]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[21]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[22]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[23]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[24]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[25]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[26]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[27]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[28]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[29]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[30]',
             '//*[@id="habillagepub"]/section[1]/section[4]/a[31]']

    if int(yr) < 2017:
        random_mois = random.choice(mois)
        if random_mois == '//*[@id="habillagepub"]/section[1]/section[2]/a[2]':
            jours28 = jours.copy()
            jours28.remove(jours28[-1])
            jours28.remove(jours28[-1])
            jours28.remove(jours28[-1])
            random_jours = random.choice(jours28)
        elif random_mois == '//*[@id="habillagepub"]/section[1]/section[2]/a[4]' or random_mois == '//*[@id="habillagepub"]/section[1]/section[2]/a[6]' or random_mois == '//*[@id="habillagepub"]/section[1]/section[2]/a[9]' or random_mois == '//*[@id="habillagepub"]/section[1]/section[2]/a[11]':
            jours30 = jours.copy()
            jours30.remove(jours30[-1])
            random_jours = random.choice(jours30)
        else:
            random_jours = random.choice(jours_2017)
    else:
        random_mois = random.choice(mois_2017)
        if random_mois == '//*[@id="habillagepub"]/section[1]/section[3]/a[2]':
            jours_28 = jours_2017.copy()
            jours_28.remove(jours_28[-1])
            jours_28.remove(jours_28[-1])
            jours_28.remove(jours_28[-1])
            random_jours = random.choice(jours_28)
        elif random_mois == '//*[@id="habillagepub"]/section[1]/section[3]/a[4]' or random_mois == '//*[@id="habillagepub"]/section[1]/section[3]/a[6]' or random_mois == '//*[@id="habillagepub"]/section[1]/section[3]/a[9]' or random_mois == '//*[@id="habillagepub"]/section[1]/section[3]/a[11]':
            jours_30 = jours.copy()
            jours_30.remove(jours_30[-1])
            random_jours = random.choice(jours_30)
        else:
            random_jours = random.choice(jours)

    time.sleep(5)
    annee_button = browser.find_element(By.LINK_TEXT, yr)
    annee_button.click()
    time.sleep(5)
    mois_button = browser.find_element(By.XPATH, random_mois)
    mois_button.click()
    time.sleep(5)
    jour_button = browser.find_element(By.XPATH, random_jours)
    jour_button.click()

    try:
        browser.find_element(By.XPATH, '//*[@id="river"]')
        article = browser.find_element(By.XPATH, '//*[@id="river"]/section[1]/a')
        article.click()
        first = False
        return browser.current_url
    except:
        get_random_article(first, yr)


def get_article_text(first, link):
    if first:
        user = ''  # left blank for privacy
        password = ''  # left blank for privacy

        button = browser.find_element(By.XPATH, '//*[@id="Header"]/header/div/div[3]/div/a[1]')
        button.click()
        time.sleep(5)

        email = browser.find_element(By.XPATH, '//*[@id="email"]')
        passcode = browser.find_element(By.XPATH, '//*[@id="password"]')
        email.send_keys(user)
        passcode.send_keys(password)

        button = browser.find_element(By.XPATH, '//*[@id="login"]/main/form/div[5]/input')
        button.click()
        time.sleep(5)

    text = browser.find_element(By.XPATH, '//*[@id="habillagepub"]/section/section[1]/article').text
    ptrn = r"[^a-zA-ZÀÁÄàáäÉÈËÊéèëêÙùÜüçÇ']"
    text = re.sub(ptrn, ' ', text)
    text = re.sub(' +', ' ', text)
    return text


def write_to_file(an, text):
    text = text.lower()
    file_name = str(an)
    file_name += '.txt'
    if 1960 <= an <= 1969:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1960s\Journals", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(text)
        file.close()
    if 1970 <= an <= 1979:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1970s\Journals", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(text)
        file.close()
    if 1980 <= an <= 1989:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1980s\Journals", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(text)
        file.close()
    if 1990 <= an <= 1999:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\1990s\Journals", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(text)
        file.close()
    if 2000 <= an <= 2009:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\2000s\Journals", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(text)
        file.close()
    if 2010 <= an <= 2019:
        file_path = os.path.join(r"G:\My Drive\Fall2021\FC 342\Final project\2010s\Journals", file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(text)
        file.close()


for year in annees:
    if year == 1960:
        print('Selecting a random article for the year {}...'.format(year))
        random_link = get_random_article(True, str(year))
        print('Article selected. Scraping article text...')
        txt = get_article_text(True, random_link)
        print('Article scraped. Writing to file...')
        write_to_file(year, txt)
        print('File created.')
    else:
        print('Selecting a random article for the year {}...'.format(year))
        random_link = get_random_article(False, str(year))
        print('Article selected. Scraping article text...')
        txt = get_article_text(False, random_link)
        print('Article scraped. Writing to file...')
        write_to_file(year, txt)
        print('File created.')

print('Process finished.')

