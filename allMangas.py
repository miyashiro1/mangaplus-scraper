from bs4 import BeautifulSoup
from selenium import webdriver
import time

links = []
names = []
dic = {}


def mangaPlus():
    global links
    global names
    global dic
    start_time = time.time()

    ##url to scrape
    urlpage = r'https://mangaplus.shueisha.co.jp/manga_list/all'
    url = 'https://mangaplus.shueisha.co.jp'
    # run firefox webdriver from executable path of your choice
    driver = webdriver.Firefox(executable_path=r'geckodriver/geckodriver.exe')
    # to go web page
    driver.get(urlpage)

    time.sleep(2)

    # retrive html so i can parse with beautifulsoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    mangas = soup.find_all('img', {'class': 'AllTitle-module_image_JIEI9'})
    manga_name = soup.find_all('div', {'class': 'AllTitle-module_allTitle_1CIUC'})

    for link in mangas:
        links.append(url + link['data-src'][36:42]+'s'+link['data-src'][42:50])

    names = [name.find('p').text for name in manga_name]

    # iterate through the 2 lists and create a dictionary like <manga title: link>
    for name, link in zip(names, links):
        # manga title starting with '2' is in spanish, and i want the english ones
        if int(link[-7]) == 2:
            continue
        else:
            dic[name] = link

    print(f'--- {time.time() - start_time} seconds ---')
    driver.quit()
