'''
Author: Otoya
Date: 2022-10-14 15:26:41
LastEditors: Otoya
LastEditTime: 2022-10-14 19:27:33
FilePath: \codehub\python\opencv-NoobPython\code\MouseBack.py
Description: 
by windows11
hello ,world
Copyright (c) Otoya
'''
#需求：
# 创建一幅大小为500*500白色图像
# 第一次单击鼠标左键
# 以当前鼠标为起点,绘制长为50的蓝色直线
# 第二次单击鼠标左键
# 以当前鼠标为矩形左上角点,绘制长为100,宽为80的实心的绿色矩形
# 第三次单击鼠标左键
# 以当前鼠标为圆心,绘制半径为50空心的线宽度为2,线颜色为红色的圆
# 依次循环
# 第四次单击鼠标右键
# 清空绘制的内容

#导入库
import cv2 as cv
import numpy as np

#定义鼠标回调函数
def draw(event,x,y,flag,parm):
    global num
    if event == cv.EVENT_LBUTTONDOWN:
        num += 1
        if num % 3 == 1:
            cv.line(img,(x,y),(x+50,y+50),(255,0,0),5)
            print("第%d次按下左键,绘制直线" % num)
        elif num % 3 == 2:
            cv.rectangle(img,(x,y),(x+100,y+80),(0,255,0),-1)
            print("第%d次按下左键,绘制直线" % num)
        elif num % 3 == 0:
            cv.circle(img,(x,y),50,(0,0,255),2)
            print("第%d次按下左键,绘制直线" % num)
            num = 0
#右键清空画布
    elif event == cv.EVENT_RBUTTONDOWN:
        img[:] = 255
    cv.imshow("img",img)


# 绘制画布
# 高宽500，三通道
img = np.zeros((500,500,3),np.uint8)+255
#定义计数器
num = 0
#命名窗口
cv.namedWindow('img')
#调用回调函数
cv.setMouseCallback('img',draw)
#显示画布
cv.imshow("img",img)
#等待
cv.waitKey(0)





# def draw(event,x,y,flag,param):
# #全局变量
#     global xys
#     global num
# # #单击鼠标左键
#     if event == cv.EVENT_LBUTTONDOWN:
# #计数器+1
#         cv.line(img,(x,y),(x+50,y+50),(255,0,0),5)
#         num += 1
#         print("第%d次按下左键，绘制直线" % num)
#         if event == cv.EVENT_LBUTTONDOWN:
#             cv.imgcp
#             cv.rectangle(img,(x,y),(x+100,y+80),(0,255,0),-1)
#             num += 1
#             print("第%d次按下左键,绘制直线" % num)
#     cv.imshow("img",img)
