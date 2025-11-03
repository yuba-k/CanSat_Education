import cv2

#変数定義
filepath = "../../data/img/" #パスの指定
filename = "200cm.jpg"
red1_low = (0, 100, 100)#H:色相/S:彩度/V:明度の順
red1_high =  (10, 255, 255)
red2_low = (170, 100, 100)
red2_high = (180, 255, 255)

img = cv2.imread(filepath+filename)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask1 = cv2.inRange(hsv,red1_low,red1_high)
mask2 = cv2.inRange(hsv,red2_low,red2_high)
mask = cv2.bitwise_or(mask1, mask2)
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("result.jpg",masked)