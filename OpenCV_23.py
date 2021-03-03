# Blend image using image pyramid:
# Step 1. load the images needed
# Step 2. find the gaussian pyramid for the image (In this example level=6)
# Step 3. find their laplacian pyramid
# Step 4. joint left and right of the two images in laplacian pyramid
# Step 5. from the joint image pyramids, reconstruct original image
import cv2 as cv
import numpy as np
# Step 1 - load images
apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
# Step 2 - Gaussian pyramid
# apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


# Orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


# Step 3 - Laplacian Pyramid
# Apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    gaus_ex = cv.pyrUp(gp_apple[i])
    lap = cv.subtract(gp_apple[i-1], gaus_ex)
    lp_apple.append(lap)


# Orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    gaus_ext = cv.pyrUp(gp_orange[i])
    lap = cv.subtract(gp_orange[i-1], gaus_ext)
    lp_orange.append(lap)


# Step 4 - Joint left and right of laplacian level
apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Step 5 - Reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1, 6, 1):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('apple_orange', apple_orange)
cv.imshow('Blending', apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()
