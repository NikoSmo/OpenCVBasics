import cv2

# Load two images
img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainlogo.png')


def overlayImages(img1, img2, x_pos=0, y_pos=0):

    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img2.shape
    roi = img1[x_pos:rows + x_pos, y_pos:cols + y_pos]

    # Now create a mask of logo and create its inverse mask
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # add a threshold
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[x_pos:rows + x_pos, y_pos:cols + y_pos] = dst
    return img1


overlayedImage = overlayImages(img1, img2, 0, 0)

cv2.imshow('overlayedImage', overlayedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
