import numpy as np
import cv2

cap = cv2.VideoCapture('videos/people-walking.mp4')
#cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
## Alternative
#fgbg_knn = cv2.createBackgroundSubtractorKNN()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    #fgmask_knn = fgbg_knn.apply(frame)
    median_blur = cv2.medianBlur(fgmask,7)

    cv2.imshow('frame',frame)
    cv2.imshow('fgmask',fgmask)
    #cv2.imshow('fgmask_knn',fgmask_knn)
    cv2.imshow('median_blur',median_blur)


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
