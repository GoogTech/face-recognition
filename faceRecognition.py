'''
Author: GoogTech
Date: 2020-12-18 19:44:25
LastEditTime: 2020-12-19 09:55:52
Description: 调用百度 AI 的一个简易人脸识别程序
Version: 0.0.1
'''
from aip import AipFace
import urllib.request
import base64
import time
import cv2
import os

# 百度人脸识别API账号信息
APP_ID = '23178422'
API_KEY = 'tzO9CzSsmGg08xwFUEEOzSsQ'
SECRET_KEY = 'B6Ls39Z7182MrkgZbRlpgU7PIwDhLpHd'
# 创建一个客户端用以访问百度云
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
# 图像编码方式
IMAGE_TYPE = 'BASE64'
# 用户组
GROUP = '01'


# 照相函数
def getimage():
    cap = cv2.VideoCapture(0)
    while 1:
        ret, frame = cap.read()
        cv2.imshow('cap', frame)
        flag = cv2.waitKey(1)
        if flag == 13:  # 按下回车键进行拍照
            output_path = os.path.join(
                "getCamera.jpg")  # 默认情况下 os.path.join 的路径为当前路径
            cv2.imwrite(output_path, frame)
            print('已拍照, 请按 Esc 键退出拍照进入验证环节 !')
            time.sleep(2)
        if flag == 27:  # 按下ESC键退出拍照
            break


# 对图片的格式进行转换
def transimage():
    f = open('getCamera.jpg', 'rb')
    img = base64.b64encode(f.read())
    return img


# 上传到百度api进行人脸检测
def go_api(image):
    result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP)
    #在百度云人脸库中寻找有没有匹配的人脸
    if result['error_msg'] == 'SUCCESS':  # 如果成功了
        name = result['result']['user_list'][0]['user_id']  # 获取名字
        score = result['result']['user_list'][0]['score']  # 获取相似度
        if score > 80:  # 如果相似度大于80
            if name == 'yu':
                print("欢迎%s !" % name)
                time.sleep(1)
        else:
            print("对不起, 我不认识你 !")
            name = 'Unknow'
            return 0
        curren_time = time.asctime(time.localtime(time.time()))  # 获取当前时间
        # 将人员出入的记录保存到Log.txt中
        f = open('Log.txt', 'a')
        f.write("Person: " + name + "     " + "Time:" + str(curren_time) +
                '\n')
        f.close()
        return 1
    if result['error_msg'] == 'pic not has face':
        print('检测不到人脸 !')
        time.sleep(3)
        return -1
    else:
        print(result['error_code'] + ' ' + result['error_code'])
        return 0


# 主函数
if __name__ == '__main__':
    while True:
        print('\n\n--------------------------------------')
        print('要开始咯~ 请面向摄像头并按下 Enter 键来拍张照片 !')
        if True:
            getimage()  # 拍照
            img = transimage()  # 转换照片格式
            res = go_api(img)  # 将转换了格式的图片上传到百度云
            if (res == 1):  # 是人脸库中的人
                print("你好 黄宇辉 !")
            else:
                print("你是谁 ? 我认不出来啊 !")
                time.sleep(2)
            print('进入下一次拍照验证环节 !')
            time.sleep(2)
