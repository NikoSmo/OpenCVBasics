import cv2
import numpy as np

img = cv2.imread('images/monkey.jpg', cv2.IMREAD_COLOR)

## Change Pixel values
#img[55,55] = [255, 255, 255]
#px = img[100:150, 100:150]
#img[100:150, 100:150] = [0, 255, 255]

# Get Image Informations
print img.shape
print img.size
print img.dtype


#Cut and Duplicate Face
face = img[100:300, 120:320]
img[0:200, 0:200] = face


cv2.imshow('cute monkey', img)

cv2.waitKey()
cv2.destroyAllWindows()
