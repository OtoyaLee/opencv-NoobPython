'''
Author: Otoya
Date: 2022-10-12 22:19:39
LastEditors: Otoya
LastEditTime: 2022-10-14 20:30:10
FilePath: \codehub\python\opencv-NoobPython\code\change_col.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''
#需求:
# 创建一幅大小为320*240（宽*高）的彩色图像
# 图像的上中下3个部分颜色依次为蓝色、绿色、红色
# 程序每隔一秒轮换3个部分的颜色

#导入库
import cv2 as cv
from cv2 import imshow
import numpy as np
#前情提要：
#   在windows中：
#       图像以矩阵储存，一张宽320，高240 像素的灰度图(单通道图/黑白图)
#       保存在一个 240*320 的矩阵中
#   而在opencv中：
#       由于要对矩阵进行计算，因此以 高 宽 载入图像
#       如需彩图，则以 高 宽 通道数 为序
#绘制画布
#创建宽高为320*240的画布
img_col = np.zeros((240,320,3),dtype=np.uint8)
#定义三个通道
c0 = 0
c1 = 1
c2 = 2
#循环条件
while True:
    img_col[:80,:,c0] = 255
    img_col[80:160,:,c1] = 255
    img_col[160:,:,c2] = 255
    cv,imshow("img_col",img_col)
#等待1s轮换
    cv.waitKey(1000)
    img_col[:,:,:] = 0
#定义中间变量
    a = c0
    c0 = c1
    c1 = c2
    c2 = a
#让窗口保持
cv.waitKey(0)
