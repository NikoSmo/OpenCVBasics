import cv2
# this is the cascade we just made. Call what you want
watch_cascade = cv2.CascadeClassifier('cascade_watch.xml')


img = cv2.imread('watch02.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

watches = watch_cascade.detectMultiScale(img, 50, 50)

# add this
for (x, y, w, h) in watches:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
