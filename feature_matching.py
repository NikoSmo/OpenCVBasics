import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('images/feature_matching.jpg', 1)
img = cv2.imread('images/tasse.jpg', 1)
#img_tmp = cv2.imread('images/feature_matching_template.jpg', 1)
img_tmp = cv2.imread('images/tasse_template.jpg', 1)

orb = cv2.ORB_create()
# Alternatives for Feature Matching
# SIFT and SURF

# find the keypoints with ORB
kp1, des1 = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(img_tmp,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img, kp1, img_tmp, kp2, matches[:5], None, flags=2)

img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB )
plt.imshow(img4)
plt.show()
