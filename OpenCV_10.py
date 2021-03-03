# Bind Track-bars to windows example 1
# for changing value of image dynamically at runtime
import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


# Create a black image and a window
img = np.zeros((300, 512, 3), dtype=np.uint8)  # img.dtype = unit8
cv.namedWindow('image')  # Create a window with a name

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0: OFF\n 1: ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while 1:
    cv.imshow('image', img)

    k = cv.waitKey(1) & 0xFF
    if k == 27:  # 27 = Esc
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv.destroyAllWindows()
