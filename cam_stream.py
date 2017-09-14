import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Set Resolution for Camera Frame
ret = cap.set(3,720)
ret = cap.set(4,480)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
