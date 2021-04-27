from PIL import Image
from pytesseract import *
import io
import pytesseract
import requests

def ocrTest(blogArray):
    k=0
    for i in blogArray:
        first = i.getImagePath().getFirstImage()
        last = i.getImagePath().getLastImage()
        sticker = i.getSticker()

        if(first != None):
            response = requests.get(first)
            img = Image.open(io.BytesIO(response.content))
            text = pytesseract.image_to_string(img, config='--psm 1', lang='kor')
            # , config='--psm 1'
            i.setFirstOCR(text.replace("\n", ' '))

        if(last != None):
            response = requests.get(last)
            img = Image.open(io.BytesIO(response.content))
            text = pytesseract.image_to_string(img, config='--psm 1', lang='kor')
            i.setLastOCR(text.replace("\n", ' '))

        if(sticker != None):
            response = requests.get(sticker)
            img = Image.open(io.BytesIO(response.content))
            text = pytesseract.image_to_string(img, config='--psm 1', lang='kor')
            i.setStickerOCR(text.replace("\n", ' '))
            print("{0} stickerOCR: {1}".format(k, i.getStickerOCR()))
        k=k+1