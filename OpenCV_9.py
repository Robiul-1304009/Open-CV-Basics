# Bitwise operators of OpenCV
import cv2 as cv
import numpy as np
# Create a black image
img1 = np.zeros((250, 500, 3), np.uint8)
# draw a while rectangular in middle of the image
img1 = cv.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
# Create second black image
img2 = np.zeros((250, 500, 3), np.uint8)
# Create a half black and half while image
img2 = cv.rectangle(img2, (250, 0), (500, 250), (255, 255, 255), -1)
# Bitwise operators
bitAND = cv.bitwise_and(img1, img2)  # AND operator
bitOR = cv.bitwise_or(img1, img2)    # OR
bitXOR = cv.bitwise_xor(img1, img2)  # XOR
bitNOT1 = cv.bitwise_not(img1)       # NOT
bitNOT2 = cv.bitwise_not(img2)       # NOT
# Show the result
cv.imshow("Image 1", img1)
cv.imshow("Image 2", img2)
cv.imshow("Bit_AND", bitAND)
cv.imshow("Bit_OR", bitOR)
cv.imshow("Bit_XOR", bitXOR)
cv.imshow("Bit_NOT1", bitNOT1)
cv.imshow("Bit_NOT2", bitNOT2)
# Close with 0
cv.waitKey(0)
cv.destroyAllWindows()
# END
