# Morphological Transformation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# img = cv.imread('Pictures\z.png', cv.IMREAD_GRAYSCALE)
img = cv.imread('Pictures/a.jpg', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, thresh=220, maxval=255, type=cv.THRESH_BINARY_INV)

k = np.ones((3, 3), dtype=np.uint8)  # kernel
di = cv.dilate(mask, kernel=k, iterations=4)  # dilation
er = cv.erode(mask, kernel=k, iterations=4)  # erosion
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel=k)  # erosion + dilation
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel=k)  # dilation + erosion
grad = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel=k)  # gradient = difference between erosion and dilation
top_hat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel=k)  # difference between image and opening of a image
black_hat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernel=k)  # difference between image and closing of a image

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient','top_hat', 'back_hat']
images = [img, mask, di, er, opening, closing, grad, top_hat, black_hat]

for i in range(9):
    plt.subplot(3, 3, i+1)  # (rows, columns, index), create a plot of 3x3=9 array subplots
    plt.imshow(images[i], cmap='gray')  # add image in plot
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

# Show the plot
plt.show()
