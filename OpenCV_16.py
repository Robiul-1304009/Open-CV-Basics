import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Pictures\Lenna.png', -1)
cv.imshow('image', img)  # BGR format
# Convert from BGR to RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)  # RGB format
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
