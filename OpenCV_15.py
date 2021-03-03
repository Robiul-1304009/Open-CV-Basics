# Adaptive Threshold
# Different threshold for different regions
import cv2 as cv
# read a image
img = cv.imread('ad.jpg', flags=0)  # 0 = grayscale image(0-255)
img = cv.resize(img, (800, 500))
# ret = 1(True) or 0(False)
# Binary Threshold
ret1, img_threshold_binary = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_BINARY)
# Adaptive threshold-ing
# Mean_C = threshold value, T(x, y) is a mean of blockSize x blockSize neighborhood of (x, y) - C(constant)
# Gaussian_C = threshold value, T(x, y) is a weighted sum of blockSize x blockSize neighborhood of (x, y) - C(constant)
img_adaptive_mean = cv.adaptiveThreshold(img, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
                                         thresholdType=cv.THRESH_BINARY, blockSize=11, C=2)

img_adaptive_gaussian = cv.adaptiveThreshold(img, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             blockSize=11, thresholdType=cv.THRESH_BINARY, C=2)

cv.imshow('Image', img)
cv.imshow('Binary', img_threshold_binary)
cv.imshow('Mean', img_adaptive_mean)
cv.imshow('Gaussian', img_adaptive_gaussian)


cv.waitKey(0)
cv.destroyAllWindows()
