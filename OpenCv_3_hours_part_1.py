# -------------------------------------------------------------------------
# Chapter 5
# Warp Perspective
import cv2

img = cv2.imread("Pictures/asami.jpg")

# print(img.shape)

cv2.imshow('image', img)

cv2.waitKey(0)  # 0 = infinite delay until press 0
cv2.destroyAllWindows()
