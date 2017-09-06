import numpy as np
import cv2


img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainlogo.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2grey, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

overlayedImage = cv2.add(img1_bg, img2_fg)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_bg', img2_fg)
cv2.imshow('overlayedImage', overlayedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
