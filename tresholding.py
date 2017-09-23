import numpy as np
import cv2


img = cv2.imread('images/bookpage.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret2, threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('normal_threshold_color', threshold)


ret, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('normal_threshold_grey', threshold2)


gaussian_threshold = cv2.adaptiveThreshold(
    grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('adaptive_threshold_gaussian', gaussian_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
