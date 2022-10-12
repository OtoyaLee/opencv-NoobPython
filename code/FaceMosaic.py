'''
Author: Otoya
Date: 2022-10-09 19:27:17
LastEditors: Otoya
LastEditTime: 2022-10-12 21:59:12
FilePath: \codehub\python\opencv-NoobPython\code\FaceMosaic.py
Description: 脸部打码
by windows11
hello ,world
Copyright (c) Otoya
'''

#需求：
# 首先读取lena图像
# 将人脸使用灰色矩形遮挡
# 将处理后的结果命名为lena_change.jpg
# 显示在窗口中并存放到当前程序路径下

#导入库
import cv2 as cv
import numpy as np
#定义鼠标回调函数，获取坐标
def draw(event,x,y,flag,param):
    #全局变量
    global xys
#单击鼠标左键，绘制当前坐标(x,y)
    if event == cv.EVENT_LBUTTONDOWN:
#whereis为putText函数的参数Text(文本内容)
        whereis='(%s,%s)'%(x,y)
#设置字体为正常的sans-serif字体,字体大小0.6,字体颜色为纯黑
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,whereis,(x,y),font,0.6,(0,0,0),1,cv.LINE_AA)
    cv.imshow("img",img)
#读取图片
img  = cv.imread("D:\codehub\python\opencv-NoobPython\img\lena.jpg")
#将鼠标获取的信息写入列表
xys = []
#显示图片
# cv.imshow("img",img)
cv.namedWindow("img")
#调用回调函数
cv.setMouseCallback("img",draw)
#等待3s后显示打码后图片
cv.waitKey(3000)
#为图像打码
#脸部区域 x为纵y为横
img[163:316,132:274]=[100,100,100]
#将图片存入out路径并重命名
cv.imwrite("D:\codehub\python\opencv-NoobPython\code\out\lean_change.jpg",img)





#让窗口保持
cv.waitKey(0)