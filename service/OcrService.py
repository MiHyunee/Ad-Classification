from PIL import Image
from pytesseract import *
import io
import pytesseract
import requests
from service.OcrProcessingService import contour
import cv2
import numpy as np

def ocrTest(blogArray):
    k=0
    a = 0
    for i in blogArray:
        last = i.getImagePath().getLastImage()
        sticker = i.getSticker()
        text=""
        try:
            if(last != None):
                response = requests.get(last)
                img = Image.open(io.BytesIO(response.content))
                #PIL image cv2 타입으로 변환
                np_img=np.array(img)
                cv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
                print(last)
                #processing
                imgArray = contour(cv_img, 3, 9, 3)
                if(len(imgArray) > 2):
                    contour(cv_img, 10, 35, 9)
                print(len(imgArray))
                if(len(imgArray)<11):
                    for fraction in imgArray:
                        #테스트 코드
                        '''
                        a=a+1
                        print(a)
                        cv2.imwrite('f'+str(a)+'.jpg',fraction)
                        '''
                        t = pytesseract.image_to_string(fraction, config='--psm 4', lang='kor')
                        text += t
                i.setLastOCR(text.replace('\n', ' '))
        except:
            i.setLastOCR("")
        print(text.replace('\n', ' ')) #테스트 코드

        try:
            if(sticker != None):
                response = requests.get(sticker)
                img = Image.open(io.BytesIO(response.content))
                text = pytesseract.image_to_string(img, config='--psm 4', lang='kor')
                i.setStickerOCR(text.replace("\n", ' '))
        except:
            i.setStickerOCR("")

        k=k+1
    return blogArray