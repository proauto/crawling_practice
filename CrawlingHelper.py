import requests
from bs4 import BeautifulSoup

# catch whole file for website
def crawling(url):

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    print(soup)

    return soup

# catch selected sentences for website
def selectCrawling(url, param):

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    print(soup)
    for link in soup.select(param):
        href = url + link.get('href')
        title = link.string
        print(href)
        print(title)

        return (soup, href, title)
