from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


def top10():
    n_names = []
    links_manga = []
    dic_manga = {}
    top10.results = []

    start_time = time.time()
    # specify the url
    urlpage = r'https://mangaplus.shueisha.co.jp/manga_list/hot'
    url = 'https://mangaplus.shueisha.co.jp'
    # run firefox webdriver from executable path of your choice
    driver = webdriver.Firefox(executable_path=r'geckodriver/geckodriver.exe')
    driver.get(urlpage)  # get web page

    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    top3_mangas = soup.find('div', {'class': 'HotTitles-module_flexContainer_2sQEA'})
    mangas = soup.find('div', {'class': 'HotTitles-module_gridContainer_2jaSS'})

    names = []

    for manga in top3_mangas:
        n_names.append(manga.find('p', {'class':'HotTitle-module_title_3jraN'}).text)
        links_manga.append(manga.get('href'))

    for manga in mangas:
        n_names.append(manga.find('p', {'class':'HotTitle-module_title_3jraN'}).text)
        links_manga.append(manga.get('href'))


    for name, link in zip(n_names, links_manga):
        if name.lower() in dic_manga:
            continue
        elif int(link[-6]) == 2:
            continue
        else:
            if len(top10.results) != 11:
                top10.results.append(f'{name}: {url + link}')

    filepath = os.path.join(r'C:*****', 'top10.txt')
    f = open(filepath, 'w', encoding='utf-8')
    f.write(', '.join(top10.results))
    f.close()


    print(f'--- {time.time() - start_time} seconds ---')
    driver.quit()
