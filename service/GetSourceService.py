import requests
from bs4 import BeautifulSoup
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath

def crawlingSource(blogArray):
    for i in range(100):
        url = blogArray[i].getPageUrl()
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, "html.parser")

        #이미지 url 얻기
        img = soup.find_all(attrs={'class': 'se-image-resource'})
        firstImage = img[0].get("src")
        firstImageWithSize = firstImage.replace('w80_blur', 'w966')
        blogArray[i].getImagePath().setFirstImage(firstImageWithSize)
        lastImage = img[-1].get("src")
        lastImageWithSize = lastImage.replace('w80_blur', 'w966')
        blogArray[i].getImagePath().setLastImage(lastImageWithSize)

        #스티커 url 얻기
        sticker = soup.find_all(attrs={'class': 'se-sticker-image'})
        if sticker:
            blogArray[i].setSticker(sticker[-1].get("src"))

        print("{0} sticker: {1}".format(i, blogArray[i].getSticker()))

