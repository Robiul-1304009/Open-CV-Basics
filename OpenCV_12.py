# HSV = Hue, Saturation, Value = Hex-cone color model = cylindrical cone model
# RGB > color luminance / intensity > HSV
# Hue = Angle(0-360) > red, yellow, green, cyan, blue, magenta
# Saturation = depth of pigment = dominance of Hue(0-100%) = 0-1 / 0-255(8-bit)
# Value = brightness of color(0-100%) = 0-1 / (0-255)
# Import cv2 and numpy libraries
import cv2 as cv
import numpy as np
# Define a function
def nothing(x):
    print(x)


# Create a named window
cv.namedWindow("Tracking")
# New window for adjusting value of hsv
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)  # For Lower Hue
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)  # For Lower Saturation
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)  # For Lower Value
cv.createTrackbar('UH', 'Tracking', 255, 255, nothing)  # For Upper Hue
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)  # For Upper Saturation
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)  # For Upper Value

while True:
    frame = cv.imread('Pictures/miya.jpg')

    # Convert to HSV image
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_hue = cv.getTrackbarPos('LH', 'Tracking')
    lower_saturation = cv.getTrackbarPos('LS', 'Tracking')
    lower_value = cv.getTrackbarPos('LV', 'Tracking')

    upper_hue = cv.getTrackbarPos('UH', 'Tracking')
    upper_saturation = cv.getTrackbarPos('US', 'Tracking')
    upper_value = cv.getTrackbarPos('UV', 'Tracking')

    # For blue, lower_hue = 100, lower_saturation = 50, lower_value = 50
    # For blue, upper_hue = 130, upper_saturation = 255, upper_value = 255
    lower_blue = np.array([110, 50, 50])  # lower limit for blue color in hsv
    upper_blue = np.array([130, 255, 255])  # upper limit for blue color in hsv
    # Lower and upper limits of color value
    lower = np.array([lower_hue, lower_saturation, lower_value])
    upper = np.array([upper_hue, upper_saturation, upper_value])

    # Threshold  of hsv image for blue color
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Threshold of hsv image for a certain color
    mask_color = cv.inRange(hsv, lower, upper)
    # And operation
    result = cv.bitwise_and(frame, frame, mask=mask)
    result_tracking = cv.bitwise_and(frame, frame, mask=mask_color)

    cv.imshow('frame', frame)
    cv.imshow('hsv', hsv)
    cv.imshow('mask', mask)
    cv.imshow('mask_color', mask_color)
    cv.imshow('result', result)
    cv.imshow('result_tracking', result_tracking)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break


cv.destroyAllWindows()
