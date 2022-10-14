#需求
# 替换背景
# 从绿幕图片中过滤出绿幕
# 将狮子从绿幕中抠出来
# 在企鹅图片上抠出狮子的位置
# 将狮子和企鹅图片进行相加得到最终的图片
# 最终图片效果如下

#导入库
from re import L
import cv2 as cv
from cv2 import imshow

#载入绿幕狮子与企鹅背景
lion = cv.imread("D:\codehub\python\opencv-NoobPython\img\lion.jpg")
qie = cv.imread("D:\codehub\python\opencv-NoobPython\img\qie.jpg")
#显示
cv.imshow("lion",lion)
cv.imshow("qie",qie)
#将狮子图片转化为hsv色彩空间
hsv_lion = cv.cvtColor(lion,cv.COLOR_BGR2HSV)
#提取狮子背景色
#并设定颜色上下限
mask = cv.inRange(hsv_lion,(35,45,46),(77,255,255))
#将提取到的背景色变为黑色
lion[mask!=0] = 0
#在企鹅背景图中将狮子处北京变为黑色
qie[mask==0] = 0
#将抠出的狮子与背景图合成
end = cv.add(lion,qie)
#显示
cv.imshow("end",end)
#等待
cv.waitKey(0)