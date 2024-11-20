import face_recognition as fr
import cv2 as cv
import json
import numpy as np
from multiprocessing import Pool, Queue
import itertools

def recognition(frame,known_face_encodings,known_face_names, tolerance=0.4):
    rgb_frame = frame[:,:,::-1]

    face_locations = fr.face_locations(rgb_frame)
    flag = 1
    if face_locations == []:
        print("No face detected")
        flag = 0
    else:
        print('people:',len(face_locations))
        print("success")
    
    if flag == 1:
        face_encodings = fr.face_encodings(frame, face_locations)
        for (top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
            name = "Unknown"
            face_distances = fr.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if face_distances[best_match_index] < tolerance:
                name = known_face_names[best_match_index]

            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv.putText(frame, name, (left + 6, bottom - 6),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    return frame



if __name__ == "__main__":
    cap = cv.VideoCapture('Video/together_1.mp4')
    if not cap.isOpened():
        print("Error opening video stream or file")
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter('Output/output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    with open('train.json','r') as f:
        data = json.load(f)
        f.close()

    known_face_names = data['names']
    known_face_encodings = [np.array(encoding) for encoding in data["encodings"]]

    buffer = []
    results = []
    #开启多线程
    tolerance = 0.5
    with Pool(processes=4) as pool:

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            buffer.append(frame)

            if len(buffer) == 4:
                result = pool.starmap(recognition,zip(
                    buffer,
                    itertools.repeat(known_face_encodings),
                    itertools.repeat(known_face_names),
                    itertools.repeat(tolerance),
                ))
                results.extend(result)
                buffer = []
            
            if results:
                for i in results:
                    out.write(i)
                    cv.imshow('Video',i)
                results = []

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv.destroyAllWindows()

