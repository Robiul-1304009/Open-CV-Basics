# Read and write video
import cv2

# cap = cv2.VideoCapture("Code\python_1.mp4")
cap = cv2.VideoCapture(0)  # 0 = default webcam
# print(cap.isOpened())
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc('X','V', 'I', 'D')
# (name, video_codex, frames_per_second, size
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(w, "\t", h)

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
