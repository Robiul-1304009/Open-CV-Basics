# Read and write image
import cv2
# print(cv2.__version__)
# Read image
img = cv2.imread("Pictures\Lenna.png", -1)  # 1= cv2.IMREAD_COLOR , 0 = grayscale -1 = unchanged including alpha channel
# Show image in windows
# print(img)
cv2.imshow("image", img)
# destroy all widows
k = cv2.waitKey(0) & 0xFF
if k == 27:  # 27 = esc button
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Write a image
    cv2.imwrite('lenna_copy.jpg', img)
    cv2.destroyAllWindows()
