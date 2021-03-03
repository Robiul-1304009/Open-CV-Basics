# Bind Track-bars to windows example 2
# for changing value of image dynamically at runtime
import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


# Create a black image and a window

cv.namedWindow('image')  # Create a window with a name

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while 1:
    img = cv.imread('lenna_copy.jpg')  # img.dtype = unit8


    k = cv.waitKey(1) & 0xFF
    if k == 27:  # 27 = Esc
        break

    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 10)

    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('image', img)


cv.destroyAllWindows()
