import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

# Set Resolution for Camera Frame
ret = cap.set(3,640)
ret = cap.set(4,480)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    mask = np.zeros(frame.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Define RoI for Foreground
    roi = (100, 100, 300, 300)

    cv2.grabCut(frame, mask, roi,  bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask == 0), 0, 1).astype('uint8')
    frame_fgd = frame*mask2[:,:,np.newaxis]

    # Display the resulting frame
    cv2.imshow('frame',frame_fgd)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
