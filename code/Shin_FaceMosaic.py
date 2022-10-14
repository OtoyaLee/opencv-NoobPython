'''
Author: Otoya
Date: 2022-10-14 20:28:30
LastEditors: Otoya
LastEditTime: 2022-10-14 20:36:13
FilePath: \codehub\python\opencv-NoobPython\code\Shin_FaceMosaic.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''

#需求:
# 对lena图像中的人脸进行马赛克处理
# 并显示马赛克的效果

#导入库
from re import I
import cv2 as cv

#载入图片
img = cv.imread("D:\codehub\python\opencv-NoobPython\img\lena.jpg")

#遍历要打马赛克的区域 
#位置寻找参考[FaceMosaic.py]
for row in range(163,326):
    for col in range(132,274):
        # 每10×10的区域将像素点颜色改成一致
        if row%10==0 and col%10==0:
            b,g,r=img[row,col]
            # 将10×10区域内的颜色值改成一致
            for i in range(10):
                for j in range(10):
                    img[row+i,col+j]=(b,g,r)
#图像显示
cv.imshow("img",img)
#等待
cv.waitKey()
