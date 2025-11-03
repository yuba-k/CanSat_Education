import cv2

filepath = ""# 画像のパスを指定
img = cv2.imread(filepath)
cv2.imshow("read",img)
cv2.waitKey(0)
cv2.imwrite("write.jpg",img)