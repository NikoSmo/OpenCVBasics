import numpy as np
import cv2

img = cv2.imread('images/corner_detection_superman.jpg')
#img = cv2.imread('images/corner_detection_sample.jpg')
#img = cv2.imread('images/corner_detection_star.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(img_gray)

corners = cv2.goodFeaturesToTrack(image= gray, maxCorners= 100, qualityLevel= 0.1, minDistance= 5)
corners = np.int0(corners)

#Alternative Edge Detectors
# cv2.cornerHarris(src, blockSize, ksize, k[, dst[, borderType]]) → dst
# cv2.cornerEigenValsAndVecs(src, blockSize, ksize[, dst[, borderType]]) → dst

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
