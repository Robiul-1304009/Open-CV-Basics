# set values to properties of video
import cv2
# Capture Video from Webcam
cap = cv2.VideoCapture(0)
# Print the width and height of the video
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 3 = default value of width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 4
# set values
cap.set(3, 33330.0)
cap.set(4, 33330.0)
# smallest = 160x120, biggest = 1280x720
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()  # read the frames from video and make ret = True(1) for video capture

    if ret == 1:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
