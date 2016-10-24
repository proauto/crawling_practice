import requests
from bs4 import BeautifulSoup

def spider(detail_url):

    url = 'http://m.blog.naver.com/hg1286/' + str(detail_url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for link in soup.select('strong > a'):
        href = "http://m.blog.naver.com" + link.get('href')
        title = link.string
        print(href)
        print(title)


def get_single_article(detail_url):
    url = 'http://m.blog.naver.com/hg1286/' + str(detail_url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for contents in soup.findAll("div",{"class" : "post_ct"}):
        print(contents.text)

spider(220542197465)
get_single_article(220542197465)
