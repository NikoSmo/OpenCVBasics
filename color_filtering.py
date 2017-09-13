import cv2
import numpy as np


img = cv2.imread('images/background_lock.jpg', cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR
lower_blue = np.array([50, 0, 0])
upper_blue = np.array([255, 255, 255])

mask_blue = cv2.inRange(hsv, lower_blue,upper_blue)
res_blue = cv2.bitwise_and(img, img, mask = mask_blue)

kernel = np.ones((15,15), np.float32) / 225
smoothed = cv2.filter2D(res_blue, -1, kernel)

# cv2.imshow('mask', mask_blue)
# cv2.imshow('blue_filter', res_blue)
cv2.imshow('mask', mask_blue)
cv2.imshow('red_filter', res_blue)
cv2.imshow('smooth', res_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
