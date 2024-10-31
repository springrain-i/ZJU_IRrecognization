import face_recognition as fr
import os
import json
path = 'Pictures/'

imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

known_face_encoding = []
known_face_names = []

for imagepath in imagePaths:
    image = fr.load_image_file(imagepath)
    face_locations = fr.face_locations(image)
    face_encodings = fr.face_encodings(image,face_locations)[0]

    known_face_encoding.append(face_encodings.tolist()) #json does not support numpy array,so convert it to list
    known_face_names.append(os.path.split(imagepath)[1].split('_')[0])

data = {
    'names':known_face_names,
    'encodings':known_face_encoding
}
with open('train.json','w') as f:
    f.write(json.dumps(data))
    f.close()

print("Training completed")