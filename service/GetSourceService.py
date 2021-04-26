import requests
from bs4 import BeautifulSoup
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath

def crawlingSource(blogArray):
    k=0
    for i in blogArray:
        url = i.getPageUrl()
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, "html.parser")

        #text 추출
        textArray = []
        text_all = soup.find(attrs={'id': 'postListBody'}).find_all('span')
        #text_all = soup.find(attrs={'class': 'se-main-container'}).find_all('span')
        for text in text_all:
            t = text.text
            if (t != '\u200b'):
                if (('#' not in t) & ('http' not in t)):
                    textArray.append(t.replace('\n', ''))

        i.setFirstText(textArray[0])
        i.setLastText(textArray[-1])

        #이미지 url 추출
        img = soup.find_all(attrs={'class': 'se-image-resource'})
        if len(img)==0:
            img = soup.find_all(attrs={'class': '_photoImage'})
        if len(img)>0:
            firstImage = img[0].get("src")
            firstImageWithSize = firstImage.replace('w80_blur', 'w966')
            i.getImagePath().setFirstImage(firstImageWithSize)
            lastImage = img[-1].get("src")
            lastImageWithSize = lastImage.replace('w80_blur', 'w966')
            i.getImagePath().setLastImage(lastImageWithSize)

        #스티커 url 추출
        sticker = soup.find_all(attrs={'class': 'se-sticker-image'})
        if sticker:
            i.setSticker(sticker[-1].get("src"))

        print("{0} sticker: {1}".format(k, i.getSticker()))
        k=k+1

