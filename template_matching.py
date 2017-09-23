import cv2
import numpy as np

#img_rgb = cv2.imread('images/template_matching_image.jpg')
img_rgb = cv2.imread('images/black_box.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#template = cv2.imread('images/template.jpg',0)
template = cv2.imread('images/black_box_template.jpg', 0)
# get width and height
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5

print(res)
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(img_rgb, pt, (pt[0], pt[1]), (0, 255, 255), 1)

cv2.imshow('Detected', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
