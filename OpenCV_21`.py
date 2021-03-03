# Image Pyramids - different resolution image - 1, 1/2, 1/4, 1/8, 1/16
# Pyramid representation is a type of multi-scale
# image\signal representation in which a image\signal
# is subject to repeated smoothing and sub-sampling.
# Types: 1. Gaussian 2. Laplacian

import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('Pictures/flower.jpg', flags=0)  # 0 = grayscale
# Gaussian Pyramid
# lower_resolution_1 = cv.pyrDown(img)  # reduce resolution of img
# lower_resolution_2 = cv.pyrDown(lower_resolution_1)  # reduce resolution of lower_resolution_1
# higher_1 = cv.pyrUp(lower_resolution_2)  # improve resolution of lower_resolution_2 - blurred image
# Gaussian = repeat filter and sub-sampling
layer = img.copy()  # copy the image
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)


cv.imshow('image', img)
# cv.imshow('PyrDown 1', lower_resolution_1)
# cv.imshow('PyrDown 2', lower_resolution_2)
# cv.imshow('PyrUp 1', higher_1)

cv.waitKey(0)
cv.destroyAllWindows()
