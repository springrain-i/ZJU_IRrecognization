import cv2 as cv
import os
import numpy as np

def getImageAndLabels(path):
    # 储存人脸数据与图片信息
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    # 加载 DNN 人脸检测模型
    modelFile = "D://withDnn//opencv_files//res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile = "D://withDnn//opencv_files//deploy.prototxt"
    net = cv.dnn.readNetFromCaffe(configFile, modelFile)

    for imagepath in imagePaths:
        img = cv.imread(imagepath)
        h, w = img.shape[:2]

        # 预处理图像以适合 DNN 模型
        blob = cv.dnn.blobFromImage(cv.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)

        detections = net.forward()

        # 迭代检测结果
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # 设置可信度阈值
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")

                face = img[y:y1, x:x1]
                gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)

                # 将人脸数据保存为训练样本
                id = int(os.path.split(imagepath)[1][0])  # 假设文件名以ID开头
                facesSamples.append(gray)
                ids.append(id)

    return facesSamples, ids

path = "D://withDnn//ZJU_IRrecognization//train_data"
faces, ids = getImageAndLabels(path)

# 使用 LBPH 识别器进行训练
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))
recognizer.write("D://withDnn//ZJU_IRrecognization//trainer.yml")
print("Completely write!")