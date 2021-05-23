from PIL import Image
from pytesseract import *
import io
import pytesseract
import requests

def ocrTest(blogArray):
    k=0
    for i in blogArray:
        last = i.getImagePath().getLastImage()
        sticker = i.getSticker()

        try:
            if(last != None):
                response = requests.get(last)
                img = Image.open(io.BytesIO(response.content))
                text = pytesseract.image_to_string(img, config='--psm 1', lang='kor')
                i.setLastOCR(text.replace("\n", ' '))
        except:
            i.setLastOCR("")

        try:
            if(sticker != None):
                response = requests.get(sticker)
                img = Image.open(io.BytesIO(response.content))
                text = pytesseract.image_to_string(img, config='--psm 1', lang='kor')
                i.setStickerOCR(text.replace("\n", ' '))
        except:
            i.setStickerOCR("")
        k=k+1
    return blogArray