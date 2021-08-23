from PIL import Image
from pytesseract import *
import io
import pytesseract
import requests
import cv2
import numpy as np

class OcrService:

    def _bwization(self, img, thres):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        r, dst = cv2.threshold(gray, thres, 255, cv2.THRESH_BINARY_INV)

        return dst

    def _contour(self, rgb, ec, rec_w, rec_h):
        gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ec, ec))
        grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        _, bw = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (rec_w, rec_h))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        mask = np.zeros(bw.shape, dtype=np.uint8)
        img = []
        for idx in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx])
            cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
            r = float(cv2.countNonZero(mask[y:y + h, x:x + w])) / (w * h)
            if r > 0.5 and w > 15 and h > 9:
                img.append(rgb[y:y + h, x:x + w])

        return img

    def ocr_lastImg(self, i):
        last = i.getImagePath().getLastImage()
        text = ""
        bw_text = ""

        try:
            if (last != None):
                response = requests.get(last)
                img = Image.open(io.BytesIO(response.content))
                # PIL image cv2 타입으로 변환
                np_img = np.array(img)
                cv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)

                # processing2
                imgArray = self._contour(cv_img, 3, 9, 3)
                if (len(imgArray) > 2):
                    self._contour(cv_img, 10, 35, 9)
                if (len(imgArray) < 11):
                    for fraction in imgArray:
                        t = pytesseract.image_to_string(fraction, config='--psm 4', lang='kor')
                        text += t

                        # 흑백처리 (임계값 임의로 230으로 설정)
                        bw_frac = self._bwization(fraction, 230)
                        bw_t = pytesseract.image_to_string(bw_frac, config='--psm 4', lang='kor')
                        bw_text += bw_t

                i.setLastOCR(text.replace('\n', ' '))
                i.setLastOCRbw(bw_text.replace('\n', ' '))
        except:
            i.setLastOCR(text)
            i.setLastOCRbw(bw_text)

        return i

    def ocr_sticker(self, i):
        sticker = i.getSticker()

        try:
            if (sticker != None):
                response = requests.get(sticker)
                img = Image.open(io.BytesIO(response.content))
                text = pytesseract.image_to_string(img, config='--psm 4', lang='kor')
                i.setStickerOCR(text.replace("\n", ' '))
        except:
            i.setStickerOCR("")

        return i