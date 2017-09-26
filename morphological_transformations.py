import cv2
import numpy as np


img = cv2.imread('images/fanta_logo.jpg', cv2.IMREAD_COLOR)
img_resized = cv2.resize(img, None, fx=0.25, fy=0.25,
                         interpolation=cv2.INTER_CUBIC)
hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)

# BGR
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(img_resized, img_resized, mask=mask)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(mask, kernel, iterations=1)
dilation = cv2.dilate(mask, kernel, iterations=1)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# It is the difference between input image and Opening of the image
# cv2.imshow('Tophat',tophat)

# It is the difference between the closing of the input image and input image.
# cv2.imshow('Blackhat',blackhat)

cv2.imshow('Original', img_resized)
cv2.imshow('Mask', res)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
