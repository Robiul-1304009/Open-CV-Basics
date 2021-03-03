# Smoothing or blurring images
# -common use is to remove noise
# Homogeneous filter, Gaussian filter, Median filter, Bilateral filter
# Homogeneous filter is the most simple filter,
# each output pixel is the mean of its kernel neighbors
# Libraries:
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
# Read Image in BGR format-
img = cv.imread('Pictures/Lenna.png')
# Convert color from BGR to RGB format-
img = cv.cvtColor(img, code=cv.COLOR_BGR2RGB)
# Kernel 1/25 (5x5)
k = np.ones(shape=(5, 5), dtype=np.float32)/25
# Homogeneous filter = filter2D
dst_img = cv.filter2D(img, -1, kernel=k)
# LPF blurring, HPF edge detection
# Averaging algorithm: blur method
blur = cv.blur(img, (5, 5))
# Gaussian filter is nothing but using different-weight-kernel in x and y
gausssian = cv.GaussianBlur(img, (5, 5), 0)  # used to remove high frequency noise
# Median filter replace each pixel's value with median of its neighboring pixels
median = cv.medianBlur(img, 5)  # ksize = 5 can be odd except 1
# used to dealing with "salt and pepper" noise
# salt and pepper noise: impulse noise
# caused by sharp and sudden disturbances in image signal
# presents itself as sparsely occurring white and black pixels
# Bilateral filter - keep image edge sharp + remove noises
bilateral = cv.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)  # d = diameter around pixel

titles = ['Image', '2D Convolution', 'Blur', 'Gaussian', 'Median', 'Bilateral']
images = [img, dst_img, blur, gausssian, median, bilateral]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
