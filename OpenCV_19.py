# Image gradient = directional change in the intensity or color in an image
# gradient laplacian derivatives, sobel method
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('sudoku.jpg', flags=0)  # 0 = grayscale
lap = cv.Laplacian(img, ddepth=cv.CV_64F, ksize=3)  # CV_64F = data-type = 64 bit float
# due to negative slope induced by transforming image from white to black
# so need to use absolute
lap = np.uint8(np.absolute(lap))
# sobel x and y
sob_x = cv.Sobel(img, cv.CV_64F, dx=1, dy=0, ksize=3)
sob_y = cv.Sobel(img, cv.CV_64F, dx=0, dy=1, ksize=3)

sob_x = np.uint8(np.absolute(sob_x))
sob_y = np.uint8(np.absolute(sob_y))
sob = cv.bitwise_or(sob_x, sob_y)

titles = ['Image', 'Laplacian', 'Sobel_X', 'Sobel_Y', 'Sobel_OR']
images = [img, lap, sob_x, sob_y, sob]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
