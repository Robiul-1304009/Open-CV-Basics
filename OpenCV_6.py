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
    # Print co-ordinate for left button click
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_PLAIN
        x_y = str(x) + ', ' + str(y)
        cv2.putText(img, x_y, org=(x, y), fontFace=font, fontScale=1, color=(255, 255, 0), thickness=1)
        cv2.imshow("MOUSE_EVENTS", img)
    # Print BGR channel for right button click
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_PLAIN
        bgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, bgr, org=(x, y), fontFace=font, fontScale=1, color=(0, 255, 255), thickness=1)
        cv2.imshow("MOUSE_EVENTS", img)


# img = np.zeros((512, 512, 3))
img = cv2.imread("Pictures\Lenna.png")
cv2.imshow("Lenna", img)

cv2.setMouseCallback('Lenna', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
