'''
Author: Otoya
Date: 2022-10-14 20:37:31
LastEditors: Otoya
LastEditTime: 2022-10-14 21:08:56
FilePath: \codehub\python\opencv-NoobPython\code\Beauty.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''

#需求:
#通过普通直方图均衡化的方法
#和使用限制对比度自适应直方图均衡化的方法
#对clahe.jpg图像进行美化操作
#展示原图、两种方式美化后的效果图
#以及原图直方图、两种方法美化后的直方图


#导入库
import cv2 as cv
import matplotlib.pyplot as plt
from numpy import r_

#载入图片
img = cv.imread("D:\codehub\python\opencv-NoobPython\img\clahe.jpg")
#显示图片
cv.imshow("img",img)
#通道分离
b,g,r = cv.split(img)
# 分别进行直方图均衡化
b_chan = cv.equalizeHist(b)
g_chan = cv.equalizeHist(g)
r_chan = cv.equalizeHist(r)
#合并通道
img_com = cv.merge([b_chan,g_chan,r_chan])
#显示直方图均衡化后的图像
cv.imshow('qualizeHist',img)
#创建【限制对比自适应直方图】对象，简称clahe，对比阈值设置为5
clahe = cv.createCLAHE(clipLimit=5)
# 分别进行clahe化
b_chan1 = clahe.apply(b)
g_chan1 = clahe.apply(g)
r_chan1 = clahe.apply(r)
#合并通道
img_clahe = cv.merge([b_chan1,g_chan1,r_chan1])
#显示clahe化后的图像
cv.imshow("clahe",img_clahe)
#等待
cv.waitKey(0)

