# Add necessary Libraries
import cv2
import numpy as np
print("Package Imported")

#------------------- Chapter 1 ---------------------
# Read a image
img = cv2.imread("Pictures\Lenna.png")

cv2.imshow("Test_image - Press 0 to close.", img)
cv2.waitKey(0)  # 0 = infinite delay until press 0

# Read a video
cap = cv2.VideoCapture("Code\python_1.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Read through web-camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # 3 = width
cap.set(4, 720)  # 4 = height
cap.set(10, 100)  # 10 = brightness

while True:
    success, img = cap.read()
    cv2.imshow("Web-camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Basic function
img = cv2.imread("Pictures\Lenna.png")
# covert to gray-scale image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur a image
img_blur = cv2.GaussianBlur(img_gray, (7, 7), sigmaX=0)  # (image, kernel, sigma
# Edge detection using Canny Edge detector
imgCanny = cv2.Canny(img_gray, 150, 200)  # (image, threshold_1, threshold_2)

cv2.imshow("Gray", img_gray)
cv2.imshow("Blur", img_blur)
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)  # 0 = infinite delay until press 0

# ------------------------------------------------------------------------------------------#
# Chapter 2
# Basic function - 2
img = cv2.imread("Pictures\Lenna.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), sigmaX=0, sigmaY=0)  # (image, kernel, sigmaX, sigmaY)

# Edge detection using Canny Edge detector
imgCanny = cv2.Canny(img_gray, 150, 200)  # (image, threshold_1, threshold_2)

# Dilation and Erosion of a image
kernel = np.ones((5, 5))
imgDilated = cv2.dilate(imgCanny, kernel, iterations=3)
imgEroded = cv2.erode(imgCanny, kernel, iterations=3)

cv2.imshow("Gray", img_gray)
cv2.imshow("Blur", img_blur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilated", imgDilated)
cv2.imshow("Erode", imgEroded)

cv2.waitKey(0)  # 0 = infinite delay until press 0
cv2.destroyAllWindows()

#----------------------------------
#-------------------------------------------------------------------------
# Chapter 3
# Resize and crop
img = cv2.imread("Pictures/flower.jpg")
print(img.shape)

img_resize = cv2.resize(img, (800, 500))  # width, height
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_resize.shape)

img_cropped = img_resize[0:200, 200:500]      # height, width

cv2.imshow('Re', img_resize)
cv2.imshow('Cr', img_cropped)

cv2.waitKey(0)  # 0 = infinite delay until press 0
cv2.destroyAllWindows()

#-------------------------------------------------------------------------
# Chapter 4
# Shapes and Texts

img = np.zeros((512, 512, 3), dtype=np.uint8)
# print(img.shape)
# img[:] = (255, 0, 0)
# Line
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# circle
cv2.circle(img, (400, 50), 30, (255, 0, 0), 5)
# Text
cv2.putText(img, "OPEN CV", (256, 506), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

cv2.imshow('image', img)


cv2.waitKey(0)  # 0 = infinite delay until press 0
cv2.destroyAllWindows()
