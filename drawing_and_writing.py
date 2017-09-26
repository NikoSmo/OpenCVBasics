import cv2
import numpy as np

# OpenCV uses BGR instead of RGB

img = cv2.imread('images/monkey.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (200, 250), (255, 0, 0), 5)
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
cv2.circle(img, (250, 250), 55, (0, 0, 255), -1)

pts = np.array([[10, 5], [20, 20], [30, 300], [60, 300], [90, 30]], np.int32)
# pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 255, 255), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Rocks!', (230, 230), font,
            0.3, (200, 255, 255), 1, cv2.LINE_AA)


cv2.imshow('window name', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
