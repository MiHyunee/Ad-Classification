import ssl
import urllib
import json
import requests
from bs4 import BeautifulSoup

from model.BlogPage import BlogPage

class SourceService:

    def transform_url(postArray):
        k = 0
        blogPageArray = []
        for url in postArray:
            blogPageArray.append(BlogPage())
            split = url.split('/', 5)
            blogPageArray[k].setPageUrl(
                "https://blog.naver.com/PostView.nhn?blogId=" + split[-2] + "&logNo=" + split[-1])
            k = k + 1

        return blogPageArray

    def rxCrawling(i):

        url = i.getPageUrl()
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, "html.parser")

        try:
            title = soup.find('div', {'class': 'se-title-text'}).find('span').text
        except:
            try:
                title = soup.find('div', {'class': 'title_post'}).find('span').text
            except:
                title = soup.find('div', {'class': 'htitle'}).find('span').text

        i.setTitle(title)

        try:
            textArray = []
            text_all = soup.find('div', {'class': 'se-main-container'})
            if (text_all == None):
                text_all = soup.find('div', {'id': 'postViewArea'}).find_all('span')
            else:
                text_all = text_all.find_all('span')
            for text in text_all:
                t = text.text
                if (t != '\u200b'):
                    if (('#' not in t) & ('http' not in t)):
                        tt = t.replace('\n', '').replace('\xa0', '').replace('\x0c', '')
                        if (tt != ''):
                            textArray.append(tt)

            i.setFirstText(textArray[0])
            i.setLastText(textArray[-1])

        except:
            i.setFirstText("")
            i.setLastText("")

        # 이미지 url 추출
        img = soup.find_all(attrs={'class': 'se-image-resource'})
        if len(img) == 0:
            img = soup.find_all(attrs={'class': '_photoImage'})
        if len(img) > 0:
            lastImage = img[-1].get("src")
            lastImageWithSize = lastImage.replace('w80_blur', 'w966')
            i.getImagePath().setLastImage(lastImageWithSize)

        # 스티커 url 추출
        sticker = soup.find_all(attrs={'class': 'se-sticker-image'})
        if sticker:
            i.setSticker(sticker[-1].get("src"))

        return i