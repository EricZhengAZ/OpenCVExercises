import cv2
import numpy as np

src = cv2.imread('C:\Users\hasee\Desktop\EC601EX2\OpenCV_Preperation\OpenCV_homework\Test_images\baboon.jpg')
cv2.namedWindow("Original")
cv2.imshow("Original",src)

blue,green,red = cv2.split(src)
cv2.namedWindow("Red")
cv2.imshow("Red",red)
cv2.namedWindow("Green")
cv2.imshow("Green",green)
cv2.namedWindow("Blue")
cv2.imshow("Blue",blue)
print("RGB: ",img[20,25])

YCrCb = cv2.cvtColor(src,cv2.COLOR_BGR2YCR_CB)
Y,Cb,Cr = cv2.split(YCrCb)
cv2.namedWindow("Y")
cv2.imshow("Y",Y)
cv2.namedWindow("Cb")
cv2.imshow("Cb",Cb)
cv2.namedWindow("Cr")
cv2.imshow("Cr",Cr)
print("YCrCb: ",YCrCb[20,25])

hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
Hue,Saturation,Value = cv2.split(hsv)
cv2.namedWindow("Hue")
cv2.imshow("Hue",Hue)
cv2.namedWindow("Saturation")
cv2.imshow("Saturation",Saturation)
cv2.namedWindow("Value")
cv2.imshow("Value",Value)
print("HSV: ",hsv[20,25])

cv2.waitKey(0)