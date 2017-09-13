import cv2
import numpy as np


img = cv2.imread('images/fanta_logo.jpg', cv2.IMREAD_COLOR)

img_resized = cv2.resize(img,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Original',img_resized)

hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)

# BGR
lower_blue = np.array([105, 0, 0])
upper_blue = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_blue,upper_blue)
res = cv2.bitwise_and(img_resized, img_resized, mask = mask)
cv2.imshow('Mask',res)

kernel = np.ones((15,15), np.float32) / 225
smoothed = cv2.filter2D(res, -1, kernel)
cv2.imshow('Averaging',smoothed)

blur = cv2.GaussianBlur(res,(15,15),0)
cv2.imshow('Gaussian Blurring',blur)

# Seems to have the best Performance
median_blur = cv2.medianBlur(res,15)
cv2.imshow('Median Blurring',median_blur)

bilateral_blur = cv2.bilateralFilter(res, 15, 75, 75)
cv2.imshow('Bilateral Blurring',bilateral_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()
