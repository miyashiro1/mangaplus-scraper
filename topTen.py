from bs4 import BeautifulSoup
from selenium import webdriver
import time

nomes = []
resultado = []
links_manga = []
dic_manga = {}


def top10():
    global nomes
    global links_manga
    global dic_manga
    global resultado

    start_time = time.time()
    # specify the url
    urlpage = r'https://mangaplus.shueisha.co.jp/manga_list/hot'
    url = 'https://mangaplus.shueisha.co.jp'
    # run firefox webdriver from executable path of your choice
    driver = webdriver.PhantomJS(executable_path=r'H:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(urlpage)  # get web page

    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    top3_mangas = soup.find('div', {'class': 'HotTitles-module_flexContainer_2sQEA'})
    mangas = soup.find('div', {'class': 'HotTitles-module_gridContainer_2jaSS'})

    for manga in top3_mangas:
        nomes.append(manga.find('p').text)
        links_manga.append(manga.get('href'))

    for manga in mangas:
        nomes.append(manga.find('p').text)
        links_manga.append(manga.get('href'))

    for name, link in zip(nomes, links_manga):
        if name.lower() in dic_manga:
            continue
        elif int(link[-6]) == 2:
            continue
        else:
            if len(resultado) != 11:
                resultado.append(f'{name}: {url + link}')

    # print(final)
    print(f'--- {time.time() - start_time} seconds ---')
    driver.quit()

# print(top10())