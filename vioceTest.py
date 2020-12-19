'''
Author: GoogTech
Date: 2020-12-19 11:25:26
LastEditTime: 2020-12-19 12:15:33
Description: Test The Voice Prompt
'''
import pyttsx3 as pyttsx

engine = pyttsx.init()
engine.say('人脸比对成功 ! 你是黄宇辉 !')
engine.runAndWait()
