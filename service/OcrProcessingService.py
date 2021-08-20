import cv2
import numpy as np

def bwization(img, thres):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    r, dst = cv2.threshold(gray,thres, 255, cv2.THRESH_BINARY_INV)

    return dst

def contour(rgb, ec, rec_w, rec_h):
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

