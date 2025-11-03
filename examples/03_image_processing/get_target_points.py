import cv2
import numpy as np

#変数定義
filepath = "../../data/img/" #パスの指定
filename = "200cm.jpg"
red1_low = (0, 100, 100)#H:色相/S:彩度/V:明度の順
red1_high =  (10, 255, 255)
red2_low = (170, 100, 100)
red2_high = (180, 255, 255)
coordinates_x = {}#座標保持
coordinates_y = {}
height = 1080
width = 1920

img = cv2.imread(filepath+filename)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask1 = cv2.inRange(hsv,red1_low,red1_high)
mask2 = cv2.inRange(hsv,red2_low,red2_high)
mask = cv2.bitwise_or(mask1, mask2)
masked = cv2.bitwise_and(img, img, mask=mask)

gray = cv2.cvtColor(masked,cv2.COLOR_BGR2GRAY)
_ , binary = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

temp = np.where(binary==255)
coordinates_x["top"] = temp[1][0]
coordinates_y["top"] = temp[0][0]
binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

temp = np.where(binary==255)
coordinates_x["left"] = temp[0][0]
coordinates_y["left"] = abs(height-temp[1][0])
binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)
binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

temp = np.where(binary==255)
coordinates_x["right"] = abs(width-temp[0][0])
coordinates_y["right"] = temp[1][0]

cv2.line(img,(coordinates_x["top"],coordinates_y["top"]),(coordinates_x["right"],coordinates_y["right"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
cv2.line(img,(coordinates_x["right"],coordinates_y["right"]),(coordinates_x["left"],coordinates_y["left"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
cv2.line(img,(coordinates_x["left"],coordinates_y["left"]),(coordinates_x["top"],coordinates_y["top"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)

cv2.imwrite("result.jpg",img)