'''
Author: Otoya
Date: 2022-10-14 19:29:04
LastEditors: Otoya
LastEditTime: 2022-10-14 20:27:21
FilePath: \codehub\python\opencv-NoobPython\code\Transform_Hehua.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''

# 需求:
# 对荷花图像进行以下几何变换
# 按下【0】键将荷花图像绕y轴水平翻转
# 按下【1】键将荷花图像向右移动80像素，向下移动60像素
# 按下【2】键将荷花图像宽和高都缩放为原来的50%
# 按下【3】键将荷花图像绕图像中心逆时针旋转45度，并缩小到50%
# 按下其他键，程序结束

#导入库
from statistics import mode
import cv2 as cv
import numpy as np

#载入图片
img = cv.imread("D:\codehub\python\opencv-NoobPython\img\hehua.jpg")
#显示图片
cv.imshow("img",img)
#旋转条件
while True:
#读取输入
    key = cv.waitKey()
#初始化偏移量
    dx,dy = 0,0
    if key == 48:
        img = cv.flip(img,2)
    elif key == 49:
#获取图片宽高
        height,width= img.shape[0:2]
#构建偏移量
        dx,dy = 80,60 
#构建平移变换矩阵
        matrixShift = np.float32([[1,0,dx],[0,1,dy]])
#计算变换后平移的图像
        img = cv.warpAffine(img,matrixShift,(width,height))
    elif key == 50:
#获取图片宽高
        height,width= img.shape[0:2]
#构建缩放范围
        hx,hy = 0.5,0.5
#构建缩放矩阵
        matrixShift = np.float32([[hx,0,0],[0,hy,0]])
#计算变换后缩放的图像
        img = cv.warpAffine(img,matrixShift,(width,height))
    elif key ==51:
#获取图片宽高
        height,width= img.shape[0:2]
#构建旋转范围
        angle = 45
#构建旋转缩放矩阵
        matrixShift = cv.getRotationMatrix2D((width/2,height/2),angle,0.5)
#计算变换后的图像
        img = cv.warpAffine(img,matrixShift,(width,height))
    else:
        break
    cv.imshow("img",img)



#等待
cv.waitKey(0)
