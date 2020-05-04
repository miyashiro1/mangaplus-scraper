from bs4 import BeautifulSoup
from selenium import webdriver
import time

n_names = []
results = []
links_manga = []
dic_manga = {}


def top10():
    global n_names
    global links_manga
    global dic_manga
    global results

    start_time = time.time()
    # specify the url
    urlpage = r'https://mangaplus.shueisha.co.jp/manga_list/hot'
    url = 'https://mangaplus.shueisha.co.jp'
    # run firefox webdriver from executable path of your choice
    driver = webdriver.Firefox(executable_path= r'geckodriver/geckodriver.exe')
    driver.get(urlpage)  # get web page

    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # print(soup)

    top3_mangas = soup.find('div', {'class': 'HotTitles-module_flexContainer_2sQEA'})
    mangas = soup.find('div', {'class': 'HotTitles-module_gridContainer_2jaSS'})

    for manga in top3_mangas:
        n_names.append(manga.find('p').text)
        links_manga.append(manga.get('href'))

    for manga in mangas:
        n_names.append(manga.find('p').text)
        links_manga.append(manga.get('href'))

    for name, link in zip(n_names, links_manga):
        if name.lower() in dic_manga:
            continue
        elif int(link[-6]) == 2:
            continue
        else:
            if len(results) != 11:
                results.append(f'{name}: {url + link}')

    print(f'--- {time.time() - start_time} seconds ---')
    driver.quit()