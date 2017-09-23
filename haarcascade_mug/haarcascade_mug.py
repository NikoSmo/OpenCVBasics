import numpy as np
import cv2
# this is the cascade we just made. Call what you want
mug_cascade = cv2.CascadeClassifier('cascade_mug.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # image, reject levels level weights.
    mugs = mug_cascade.detectMultiScale(gray, 50, 50)

    # add this
    for (x, y, w, h) in mugs:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
