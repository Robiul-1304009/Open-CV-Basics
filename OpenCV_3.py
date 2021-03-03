# Draw Geometric shapes
import cv2
import numpy as np

# img = cv2.imread("Pictures\Lenna.png", 1)
img = np.zeros(shape=[512, 512, 3])
# print(img)
# Draw a line(image, pt1, pt2, color(BGR), thickness=1-10-...
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 11)
# Arrowed Line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 11)
# Rectangle, here pt1 = upper left corner, pt2 = bottom right corner
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 11)  # 11 = -1 to fill the rectangle
# with color
# Circle
img = cv2.circle(img, center=(447, 63), radius=63, color=(0, 255, 0), thickness=-1)
# Text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img=img, text="OpenCv", org=(10, 500), fontFace=font, fontScale=4,
                  color=(255, 255, 255), lineType=cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
