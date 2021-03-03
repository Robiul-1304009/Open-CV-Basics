# Histogram
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Pictures/lena512color.tiff', flags=1)
# img = np.zeros(shape=(200, 200), dtype=np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), color=(255), thickness=-1)
# cv.rectangle(img, (0, 50), (100, 100), color=(127), thickness=-1)
# b, g, r = cv.split(img)
# cv.imshow('Image', img)
# cv.imshow('Image2', b)
# cv.imshow('Image3', g)
# cv.imshow('Image4', r)
# Histogram using matplotlib
# plt.hist(x=img.ravel(), bins=256, range=[0, 256])
# plt.hist(x=b.ravel(), bins=256, range=[0, 256])
# plt.hist(x=g.ravel(), bins=256, range=[0, 256])
# plt.hist(x=r.ravel(), bins=256, range=[0, 256])
# calculate Histogram
hist = cv.calcHist(img, channels=[3], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
