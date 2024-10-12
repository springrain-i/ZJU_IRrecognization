import cv2 as cv
import os
import urllib
import urllib.request

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

names=[]

def face_detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('/home/springrain-i/opencv-4.10.0/data/haarcascades/haarcascade_frontalface_default.xml')#使用opencv自带的分类器
    face = face_detector.detectMultiScale(gray) #确定人脸位置
    # (IMG,缩放倍数,检测次数,最小人脸,最大人脸) ,缩放倍数越高狂越精准,检测次数越多越准确,人脸大小格式(100,100),即最小人脸100*100像素框
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv.circle(img, (x + w//2, y + h//2), w//2, (0, 255, 0), 2)
        ids,confidence = recognizer.predict(gray[y:y+h,x:x+w])
        #print('ids:',ids,'评分',confidence)
        if confidence > 80: #评分大则不可信
            global warning_times
            warning_times += 1
            if warning_times > 100:
                warning_times = 0
                #留给手机端应用接口
            print('warning_times:',warning_times)
            cv.putText(img,'unknown_body',(x+10,y-10),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        else:
            cv.putText(img,'wait to do',(x+10,y-10),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv.imshow('result',img)
    
warning_times = 0
cap = cv.VideoCapture('Data/test.mp4') 
# cap = cv.VideoCapture(0) #0为默认摄像头

while True:
    flag,frame = cap.read()
    if not flag:
        print('NO FLAG')
        break
    face_detect(frame)
    print('WORKING')
    if ord('q') == cv.waitKey(1):
        break
        