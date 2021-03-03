# Mouse Events:
# lef click, right click, double left click etc.
# Import necessary libraries:
import numpy as np
import cv2
# All events in cv2:
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# Mouse event callback function:
def click_event(event, x, y, flags, param):
    # draw circle and connect with line for left button click
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), radius=3, color=(0, 0, 255), thickness=-1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], color=(255, 0, 0), thickness=5)
        cv2.imshow('image', img)
    #  color of the point in a image in another window for right button click
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cimg = np.zeros((512, 512, 3), dtype=np.uint8)
        cimg[:] = [blue, green, red]
        cv2.imshow('color', cimg)


# img = np.zeros((512, 512, 3))
img = cv2.imread("Pictures\Lenna.png")
cv2.imshow("Lenna", img)
points = []
cv2.setMouseCallback('Lenna', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
