import requests
from bs4 import BeautifulSoup
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath

def crawlingSource(blogArray):
    for i in range(100):
        url = blogArray[i].getPageUrl()
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, "html.parser")

        #text 추출
        text = []
        text_all = soup.find(attrs={'class': 'se-main-container'}).find_all('span')
        for i in text_all:
            t = i.text
            if (t != '\u200b'):
                if (('#' not in t) & ('http' not in t)):
                    text.append(t)

        blogArray[i].setFirstText(text[0])
        blogArray[i].setLastText(text[-1])

        #이미지 url 추출
        img = soup.find_all(attrs={'class': 'se-image-resource'})
        if len(img)==0:
            img = soup.find_all(attrs={'class': '_photoImage'})
        if len(img)>0:
            firstImage = img[0].get("src")
            firstImageWithSize = firstImage.replace('w80_blur', 'w966')
            blogArray[i].getImagePath().setFirstImage(firstImageWithSize)
            lastImage = img[-1].get("src")
            lastImageWithSize = lastImage.replace('w80_blur', 'w966')
            blogArray[i].getImagePath().setLastImage(lastImageWithSize)

        #스티커 url 추출
        sticker = soup.find_all(attrs={'class': 'se-sticker-image'})
        if sticker:
            blogArray[i].setSticker(sticker[-1].get("src"))

        print("{0} sticker: {1}".format(i, blogArray[i].getSticker()))

