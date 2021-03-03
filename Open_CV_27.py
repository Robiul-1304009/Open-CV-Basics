# The Hough(Haff) Transform - Line Transform Theory
# is a popular technique to detect any shape,
# shape that can be represented in mathematical form.
# It can detect shape that are broken or distorted.

'''

Line --- cartesian  y = mx + c, polar x cosQ + y sinQ = r
Cartesian --
slope = m, intercept = c Line in xy space;
so point (m, c) in mc space.
So its Line > point.
Now point > Line:
point (x, y) in xy space, slope = -x, intercept = y in mc space.
Polar--
Q = Angle, r = distance from origin to line
y = -(cosQ/sinQ)*x + r/sinQ
H.T transform: Polar co-ordinate system
*** Hough Transform Algorithm:
*** Steps:
1. Edge detection e.g. Canny edge detector
2. Mapping edge points to the hough space and
   storage in an accumulator.
3. Interpretation of the accumulator to yield lines of
   infinite length which is oone by thresholding and
   possibly other constraints.
4. Conversion of infinite lines to finite lines.
OpenCV H.T types:
1. The Standard Hough Transform (Hough-Lines method)
2. The Probalistic Hough Line Transform (Hough-Lines-P method)

'''

import numpy as np
import cv2 as cv

# import matplotlib.pyplot as plt

img = cv.imread('sudoku.jpg', flags=1)
gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
edges = cv.Canny(image=gray, threshold1=50, threshold2=150, apertureSize=3)
lines = cv.HoughLines(edges, rho=1, theta=np.pi / 180, threshold=200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv.line(img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=2)


cv.imshow('Sudoku', img)
cv.waitKey(0)
cv.destroyAllWindows()
