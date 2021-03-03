# Import necessary libraries - Not complete
import cv2 as cv
import numpy as np

img = cv.imread('Pictures/Kusano.jpg')


print("Shape: ", img.shape)      # returns a tuple of number of rows, columns, channels
print("Size: ", img.size)        # returns total number of pixels = rows*columns*channels
print("Data_Type: ", img.dtype)  # returns image data type

b, g, r = cv.split(img)
img = cv.merge((b, g, r))

# bear = img[100:188, 149:159]
# img[51:63, 133:143] = bear

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
