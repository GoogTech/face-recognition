'''
Author: GoogTech
Date: 2020-12-19 14:07:59
LastEditTime: 2020-12-19 15:14:37
Description: 调用电脑摄像头及使用 OpenCV 进行实时人脸及眼睛识别
Refer: https://github.com/YUbuntu0109/zihaoopencv
'''
import cv2

# 人脸分类级联
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     'haarcascade_frontalface_default.xml')
# 人眼分类级联
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                    'haarcascade_eye.xml')
# 调用摄像头摄像头
cap = cv2.VideoCapture(0)

# 持续运行, 点击 q 键退出
while (True):
    # 获取摄像头拍摄到的画面
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    img = frame
    # 用人脸级联分类器引擎在人脸区域进行脸部识别
    for (x, y, w, h) in faces:
        # 画出人脸框, 蓝色, 画笔宽度微
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 框选出人脸区域, 在人脸区域而不是全图中进行人眼检测, 节省计算资源
        face_area = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_area, 1.3, 15)
        # 用人眼级联分类器引擎在人脸区域进行人眼识别返回的 eyes 为眼睛坐标列表
        for (ex, ey, ew, eh) in eyes:
            #画出人眼框, 绿色, 画笔宽度为 1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0),
                          1)

    # 实时展示效果画面
    cv2.imshow('frame2', img)
    # 每 5 毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 最后, 关闭所有窗口
cap.release()
cv2.destroyAllWindows()
