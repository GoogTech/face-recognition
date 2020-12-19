'''
Author: GoogTech
Date: 2020-12-18 20:09:24
LastEditTime: 2020-12-19 09:57:55
Description: Get Picture From Camera
'''
import cv2
import os

i = 1
cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    cv2.imshow('cap', frame)
    flag = cv2.waitKey(1)
    if flag == 13:  # 按下 Enter 键进行拍照
        output_path = os.path.join("%04d.jpg" %
                                   i)  # 默认情况下 os.path.join 的路径为当前路径
        cv2.imwrite(output_path, frame)
        i += 1
        print('ok', output_path)
    if flag == 27:  # 按下 Esc 键退出拍照
        break
