# -------------- CANNY-EDGE-DETECTOR ---------------
# is an edge detection operator that uses a multi-stage algorithm
# to detect a wide range of edges in images
# Step 1. Noise reduction
# Step 2. Gradient calculation
# Step 3. Non-maximum suppression
# Step 4. Double threshold = threshold 1 & 2
# Step 5. Edge Tracking by Hysteresis = suppressing weak edges
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('sudoku.jpg', flags=0)  # 0 = grayscale
# threshold1, threshold2 for Hysteresis
canny = cv.Canny(img, threshold1=100, threshold2=200)


titles = ['Image', 'Canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
