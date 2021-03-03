# Laplacian Pyramid: a level in
# Laplacian Pyramid is formed by difference between that level in
# Gaussian Pyramid and expanded version of its upper level in
# Gaussian Pyramid.
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('sudoku.jpg', flags=0)  # 0 = grayscale
layer = img.copy()  # layer = level
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i+1), layer)

# for i in range(6):
#   cv.imshow(str(i), gp[i])


layer = gp[5]
up = cv.pyrUp(layer)
# cv.imshow('Upper layer', layer)
# cv.imshow('Exr layer', up)
lp = [layer]

for i in range(1, 6):
    ge = cv.pyrUp(gp[i-1])
    lap = cv.subtract(gp[i], ge)
    cv.imshow(str(i), lap)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
