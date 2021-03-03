# Draw on video
import cv2
import datetime
# Capture Video from Webcam
cap = cv2.VideoCapture(-1)  # 0 = default, -1 = black screemq
# Print the width and height of the video
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 3 = default value of width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 4

while cap.isOpened():
    ret, frame = cap.read()  # read the frames from video and make ret = True(1) for video capture

    if ret == 1:
        font = cv2.FONT_HERSHEY_DUPLEX
        text = "Width: " + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, org=(0, 30), fontFace=font, fontScale=1,
                            color=(0, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        frame = cv2.putText(frame, date_time, org=(0, 470), fontFace=font, fontScale=1,
                            color=(0, 255, 255), thickness=2, lineType=cv2.LINE_AA)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
