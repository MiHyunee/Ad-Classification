import requests
from bs4 import BeautifulSoup

def crawlingSource(blog):
    for i in range(1):
        url = blog[i][1]
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, "html.parser")

        #이미지 url 얻기
        img = soup.find_all(attrs={'class': 'se-image-resource'})
        for i in img:
            img_url = i.get('src')
            new_img = img_url.replace('w80_blur', 'w966')
            print(new_img+"\n")

        #스티커 url 얻기
        sticker = soup.find_all(attrs={'class': 'se-sticker-image'})
        for i in sticker:
            print(i.get('src')+'\n')

