import cv2 as cv
import numpy as np

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("D://withDnn//ZJU_IRrecognization//trainer.yml")
names = []

def face_detect(img):
    # 加载 DNN 模型
    modelFile = "D://withDnn//opencv_files//res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile = "D://withDnn//opencv_files//deploy.prototxt"
    net = cv.dnn.readNetFromCaffe(configFile, modelFile)

    h, w = img.shape[:2]

    # 图像预处理
    blob = cv.dnn.blobFromImage(cv.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)

    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            # 获得边界框
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")

            # 在图像中绘制边界框
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 2)

            # 提取检测到的脸部区域
            gray_face = cv.cvtColor(img[y:y1, x:x1], cv.COLOR_BGR2GRAY)

            # 使用识别器预测
            ids, confidence = recognizer.predict(gray_face)

            if confidence > 80:  # 评分越大越不可信
                global warning_times
                warning_times += 1
                if warning_times > 100:
                    warning_times = 0
                    # 在此插入报警或手机接口
                cv.putText(img, 'unknown_body', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                cv.putText(img, f'ID: {ids}', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv.imshow('result', img)

warning_times = 0
#cap = cv.VideoCapture('test_data/test.mp4')
cap = cv.VideoCapture('test_data/test2.mp4')
#cap = cv.VideoCapture(0) #0为默认摄像头
while True:
    ret, frame = cap.read()
    if not ret:
        print('Video Ended')
        break

    face_detect(frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()