from PIL import Image
from pytesseract import *
import io
import pytesseract
import requests
from service.OcrProcessingService import contour
import cv2

def ocrTest(blogArray):
    k=0
    for i in blogArray:
        last = i.getImagePath().getLastImage()
        sticker = i.getSticker()

        try:
            if(last != None):
                response = requests.get(last)
                img = Image.open(io.BytesIO(response.content))
                text=""
                #processing
                imgArray = contour(img, 3, 9, 3)
                if(len(imgArray) > 2):
                    contour(img, 10, 35, 9)
                for image in imgArray:
                    t = pytesseract.image_to_string(image, config='--psm 1', lang='kor')
                    text += t
                i.setLastOCR(text)
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