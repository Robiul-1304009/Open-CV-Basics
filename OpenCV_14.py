# BASIC THRESHOLD
# Threshold-ing is a segmentation technique used for separating an object from its background in a image
# compare each pixel of a image with a threshold value, greater or lower than threshold to separate
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# read a image
img = cv.imread('Pictures\Lenna.png', flags=0)  # 0 = grayscale image(0-255)
# ret = 1(True) or 0(False)
# Binary Threshold
ret1, img_threshold_binary = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_BINARY)
# Inverse Binary Threshold
ret2, img_threshold_binary_inverse = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_BINARY_INV)
# Trunc threshold = after reaching thresh value value remains same for rest, trunc rest
ret3, img_threshold_trunc = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_TRUNC)
# TO_ZERO = value is less than thresh value is 0, rest is 1
ret4, img_threshold_to_zero = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_TOZERO)
# Inverse of TO_ZERO
ret5, img_threshold_to_zero_inverse = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_TOZERO_INV)


# cv.imshow('Image', img)
# cv.imshow('Binary', img_threshold_binary)
# cv.imshow('Trunc', img_threshold_trunc)
# cv.imshow('To_zero', img_threshold_to_zero)
# cv.imshow('Inverse To_zero ', img_threshold_to_zero_inverse)
# cv.imshow('Inverse Binary', img_threshold_binary_inverse)

# cv.waitKey(0)
# cv.destroyAllWindows()

# Plotting the images
titles = ['Original', 'Binary', 'Binary_INVERSE', 'TRUNC', 'TO_ZERO', 'TO_ZERO_INV']
images = [img, img_threshold_binary, img_threshold_binary_inverse, img_threshold_trunc,
          img_threshold_to_zero, img_threshold_to_zero_inverse]

for i in range(6):
    plt.subplot(2, 3, i+1),
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
