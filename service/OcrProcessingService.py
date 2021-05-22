import cv2
from pytesseract import *
import pytesseract
import numpy as np

def contour():
    rgb = cv2.imread("/Users/smwu/Desktop/sample_image/full4.jpg")
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    #gray = cv2.medianBlur(gray,5)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    mask = np.zeros(bw.shape, dtype=np.uint8)
    for idx in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y + h, x:x + w] = 0  #
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y + h, x:x + w])) / (w * h)
        if r > 0.5 and w > 8 and h > 8:
            cv2.imwrite('divide'+str(x)+'.jpg',rgb[y:y+h,x:x+w])
            cv2.rectangle(rgb, (x, y), (x + w - 1, y + h - 1), (0, 255, 0), 2)


    # 이미지 저장
    cv2.imwrite('divide.jpg', rgb)

contour()
