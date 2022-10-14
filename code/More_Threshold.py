'''
Author: Otoya
Date: 2022-10-14 21:38:47
LastEditors: Otoya
LastEditTime: 2022-10-14 22:25:47
FilePath: \codehub\python\opencv-NoobPython\code\More_Threshold.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''

#需求:
# 对chess.jpg图像进行二值化阈值处理
# 反二值化阈值处理
# 二值化阈值处理+Otsu算法
# 反二值化阈值处理+Otsu算法
# 显示各种处理后效果

#导入库
import cv2 as cv
from cv2 import imread

#载入图片
img = imread("D:\codehub\python\opencv-NoobPython\img\chess.jpg",cv.IMREAD_GRAYSCALE)
#显示图片
cv.imshow("img",img)
height,width=img.shape[0:2]
#定义阈值  二值化阈值处理 >阈值，设置为255
thresh=150
for row in range(height):
    for col in range(width):
        grayVal=img[row,col]
        if grayVal>thresh:
            img[row,col]=255
        else:
            img[row,col]=0
cv.imshow("binary", img)
#二值阈值处理
th,th1=cv.threshold(img,thresh,255,cv.THRESH_BINARY)
cv.imshow("th", th1)
#反二值阈值处理
th,th2=cv.threshold(img,thresh,255,cv.THRESH_BINARY_INV)
cv.imshow("th_inv",th2)
#二值阈值处理+otsu算法
th,th3=cv.threshold(img,thresh,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("th+otsu", th3)
#反二值阈值处理+otsu算法
th,th4=cv.threshold(img,thresh,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
cv.imshow("th_inv+otsu",th4)
cv.waitKey()
