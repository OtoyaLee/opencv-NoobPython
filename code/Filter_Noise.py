'''
Author: Otoya
Date: 2022-10-14 21:09:55
LastEditors: Otoya
LastEditTime: 2022-10-14 21:37:07
FilePath: \codehub\python\opencv-NoobPython\code\Filter_Noise.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''

#需求:
# 对lena.jpg图像添加椒盐噪声
# 保存为lena_noise.jpg
# 选择合适的滤波器对lena_noise.jpg进行去噪
# 显示原图、带椒盐噪声图、去噪后的图。

#导入库
import cv2 as cv
import numpy as np

#定义椒盐噪音函数
def noise(img,n=10000):
    result = img.copy()
    height,width = img.shape[0:2]
    for i in range(n):
#分别再宽高范围内生成一个随机值，模拟x,y坐标
        x = np.random.randint(1,width)
        y = np.random.randint(1,height)
        if np.random.randint(0,2) == 0:
#生成黑色噪音
            result[x,y] = 0
        else:
#生成白色噪音
            result[x,y] = 255
    return result
#载入图片
img = cv.imread("D:\codehub\python\opencv-NoobPython\img\lena.jpg")
#调用函数
res = noise(img,10000)
# #写入
# cv.imwrite("D:\codehub\python\opencv-NoobPython\img\noise.jpg",res)
#显示椒盐噪音化后的图
cv.imshow("res",res)
#选择中值滤波方式
med = cv.medianBlur(res,3)
#显示中值滤波后的椒盐噪音
cv.imshow("medianblur",med)
#显示原图
cv.imshow("img",img)
#等待
cv.waitKey(0)

