#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os


def wiki_spider():

    # 다운로드 경로
    down_url = "https://dumps.wikimedia.org/kowiki/latest/kowiki-latest-pages-articles.xml.bz2"

    # 버전 확인을 위한 경로
    url = 'https://dumps.wikimedia.org/kowiki/latest/'
    file = "kowiki-latest-pages-articles.xml.bz2"
    current_path = os.path.abspath(os.curdir)
    meta_file = "data/meta-data.txt"
    meta_path = os.path.join(current_path, meta_file)

    # 크롤링을 통해서 버전이 일치하는지 확인
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')

    # 과거 버전 존재 확인
    if(os.path.isfile(meta_path)):
        old_row = open(meta_path,'r').readline()
    else:
        os.makedirs(current_path+"/data/")
        f = open(meta_path, 'a+')
        old_row = ""


    # 버전 일치 확인
    for row in soup.get_text().splitlines():
        row_sp = row.split(' ',2)
        if(row_sp[0] == file):
            # 버전 일치하면 그대로
            if(row == old_row):
                print("변경 사항 없음")
            # 버전이 다르면 위키피디아 데이터 덤프를 가져옴 - 현재는 다운로드 경로 - 훗날 이동시킬 것
            else:
                f = open(meta_path, 'w')
                f.write(str(row))
                f.close()
                print("새로운 값으로 변경")
                os.system("python -m webbrowser -t \"" + down_url + "\"")



wiki_spider()

