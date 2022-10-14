'''
Author: Otoya
Date: 2022-10-14 22:26:57
LastEditors: Otoya
LastEditTime: 2022-10-14 23:12:05
FilePath: \codehub\python\opencv-NoobPython\code\Shape.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''

#需求:
# 对shapes.jpg图形进行查找所有轮廓
# 绘制所有轮廓
# 绘制所有轮廓的轮廓的最小外包圆
# 输出所有轮廓的面积、周长

#导入库
from concurrent.futures import thread
import cv2 as cv
import numpy as np

#载入图片
img = cv.imread("D:\codehub\python\opencv-NoobPython\img\shapes.jpg")
#显示原图
cv.imshow('img',img) 
#转为灰度图
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)	
#二值域化
thresh,img2=cv.threshold(gray,125,255,cv.THRESH_BINARY)
#查找轮廓
c,h=cv.findContours(img2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#绘制原图大小的白色画布
# img3=np.zeros(img.shape,np.uint8)+255
# img3=cv.drawContours(img3,c,-1,(0,0,255),2)
# cv.imshow("img3",img3)
for n in(range(len(c))):
#绘制原图大小的白色画布
    img3 = np.zeros(img.shape,np.uint8)+255
#绘制轮廓
    cv.polylines(img3,[c[n]],True,(255,0,0),2)
#显示轮廓图像
    cv.imshow('%s' % n,img3)
    area = cv.contourArea(c[n])
    print("轮廓%s的面积"%n,area)
    length = cv.arcLength(c[n],True)
    print("轮廓%s的周长"%n,length)
#计算最小外包圆
    (x,y),r = cv.minEnclosingCircle(c[n])
    center = (int(x),int(y))
    r = int(r)
#绘制最小外包圆
    cv.circle(img3,center,r,(255,0,0),2)
#绘制轮廓
    cv.polylines(img3,[c[n]],True,(255,0,0),2)
#显示轮廓
    cv.imshow('%s' % n,img3)
#等待
cv.waitKey(0)