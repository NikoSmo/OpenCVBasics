import numpy as np
import cv2
import time

img = cv2.imread('images/cat.jpg')
img = cv2.imread('images/god.jpg')

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=19)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=19)

edges = cv2.Canny(img, 150, 250)


while True:

    cv2.imshow('Original', img)
    cv2.imshow('Laplacian', laplacian)
    cv2.imshow('SobelX', sobelx)
    cv2.imshow('SobelY', sobely)
    cv2.imshow('Edges', edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
