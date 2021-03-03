# Find and draw contours
import cv2 as cv
import numpy as np

image = cv.imread('opencv-logo.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# contour = is a python list of all contours in the image
ret, th = cv.threshold(gray, thresh=127, maxval=255, type=0)

contours, Heircial = cv.findContours(th, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

print("Number of contours: ", str(len(contours)))
print(contours[0])

cv.drawContours(image, contours=contours, contourIdx=-1, color=(0,255, 255), thickness=5)

cv.imshow('Image', image)
cv.imshow('Gray', gray)

cv.waitKey(0)
cv.destroyAllWindows()

