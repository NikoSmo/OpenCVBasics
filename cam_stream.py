import cv2

cap = cv2.VideoCapture(0)

# Set Resolution for Camera Frame
ret = cap.set(3, 720)
ret = cap.set(4, 480)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, 20, 3, 10)
    cv2.imshow('corners', dst)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
