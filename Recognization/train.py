import cv2 as cv
import os
from PIL import Image
import numpy as np
def getImageAndLabels(path):
    # 储存人脸数据与图片信息
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    face_detector = cv.CascadeClassifier('/home/springrain-i/opencv-4.10.0/data/haarcascades/haarcascade_frontalface_default.xml')
    
    for imagepath in imagePaths:
        PIL_img = Image.open(imagepath).convert('L') #打开灰度图
        matrix_img = np.array(PIL_img,'uint8') #将灰度信息转换为数组
        face = face_detector.detectMultiScale(matrix_img) #获取人脸部位
        id = int(os.path.split(imagepath)[1][0]) #存疑

        for x,y,w,h in face:
            ids.append(id)
            facesSamples.append(matrix_img[y:y+h,x:x+w])
    print('id:',id)

    return facesSamples,ids

path = '/home/springrain-i/face/Data/'
faces,ids = getImageAndLabels(path)
#加载识别器

recognizer = cv.face.LBPHFaceRecognizer_create()

recognizer.train(faces,np.array(ids))

recognizer.write("trainer/trainer.yml")

