from __future__ import print_function
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol
import numpy as np
import cv2
# from Tkinter import *

def decode(img):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(img)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects


# Display barcode and QR code location
def drawCodes(img, decodedObjects):
    # Loop over all decoded objects
    centerPoint = None
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(
                np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(img, hull[j], hull[(j+1) % n], (255, 0, 0), 3)
        
        # Find and Draw Center Point
        pointArray = np.array([point for point in points])
        M = cv2.moments(pointArray)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        centerPoint = (cx, cy)
        cv2.circle(img, centerPoint, radius = 5, color = (0, 255, 255), thickness= -1)

    # Display results
    return img, centerPoint

def editImage(img):

    # Sectoring 
    cv2.line(img, (0, height // 2), (width, height // 2), (0, 255, 0), 5)
    cv2.line(img, (width // 2, 0), (width // 2, height), (0, 255, 0), 5)

    # name Sectors
    font = cv2.FONT_HERSHEY_PLAIN
    width_offset= 10
    height_offset = 10
    cv2.putText(img, "1", (width_offset, height // 2 - height_offset), font, fontScale=6, color=(255, 0, 0), thickness = 5 )
    cv2.putText(img, "2", (width // 2 + width_offset, height // 2 - height_offset), font, fontScale=6, color=(255, 0, 0), thickness = 5 )
    cv2.putText(img, "3", (width_offset, height - height_offset), font, fontScale=6, color=(255, 0, 0), thickness = 5 )
    cv2.putText(img, "4", (width // 2  + width_offset, height - height_offset), font, fontScale=6, color=(255, 0, 0), thickness = 5 )

    #cv2.putText(img, "Dachser", (width // 2,  50), font, fontScale=5, color=(0, 0, 255))
    # impose Dachser Logo on Image
    logo = cv2.imread("dachserLogo.jpg")
    logoSmall = cv2.resize(logo, dsize=None, fx=0.2, fy=0.2)
    height_offset = 0
    width_offset = width // 2 - logoSmall.shape[1] // 2
    img[height_offset:height_offset+logoSmall.shape[0], width_offset:width_offset+logoSmall.shape[1]] = logoSmall


    return img

def findCodeSector(img, centerPoint):
    height, width, channels = img.shape
    if centerPoint[0] <=  width // 2 and centerPoint[1] <= height // 2:
        sector = 1
    elif centerPoint[0] >  width // 2 and centerPoint[1] <= height // 2:
        sector = 2
    elif centerPoint[0] <=  width // 2 and centerPoint[1] > height // 2:
        sector = 3
    elif centerPoint[0] >  width // 2 and centerPoint[1] > height // 2:
        sector = 4
    return sector

# class App:
#   def __init__(self, master):
#     frame = Frame(master)
#     frame.pack()
#     self.button = Button(frame, 
#                          text="QUIT", fg="red",
#                          command=frame.quit)
#     self.button.pack(side=LEFT)
#     self.slogan = Button(frame,
#                          text="Hello",
#                          command=self.write_slogan)
#     self.slogan.pack(side=LEFT)
#   def write_slogan(self):
#     print("Tkinter is easy to use!")


# Main
if __name__ == '__main__':
    # TODO : Pipe Communication
    # TODO : GUI -> Probably gonna use PyGame for that

    # root = Tk()
    # app = App(root)
    # root.mainloop()

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)


    # Message Consists of : QR Code Data, CenterPoint of QRCode and Sector it is in
    ret, img = cap.read()
    height, width, channels = img.shape
    while(True):
        ret, img = cap.read()
        # decodedObjects = decode(img)
        decodedObjects = pyzbar.decode(img, symbols=[ZBarSymbol.QRCODE])
        img = editImage(img)

        if decodedObjects:
            img, centerPoint = drawCodes(img, decodedObjects)

            if centerPoint is not None:
                sector = findCodeSector(img, centerPoint)
                print(sector)
                # Message for Laser
                QRCodeData = decodedObjects[0][0].decode('UTF-8')
                msg = "{},({};{}),{}".format(QRCodeData, centerPoint[0], centerPoint[1], sector)

        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
