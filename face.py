import face_recognition as fr
import cv2 as cv
import json
import numpy as np
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

face_locations = []
face_encodings = []
face_names = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:,:,::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = fr.face_locations(frame)
    if face_locations == []:
        print("No face detected")
        continue
    else:
        print('len:',len(face_locations))
        print("success")
    
    face_encodings = fr.face_encodings(frame, face_locations)
    face_names = []

    for (top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
        # See if the face is a match for the known face(s)
        name = "Unknown"
        matches = fr.compare_faces(known_face_encodings, face_encoding) 
        face_distances = fr.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv.putText(frame, name, (left + 6, bottom - 6),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)     

    out.write(frame)
    # Display the resulting image
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()