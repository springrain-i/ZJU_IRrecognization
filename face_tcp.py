import asyncio
import websockets
import cv2
import json
import numpy as np
from picamera2 import Picamera2
import face_recognition as fr

# Initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())
picam2.start()

# Load known faces from JSON
with open('train_night.json', 'r') as f:
    data = json.load(f)
known_face_names = data['names']
known_face_encodings = [np.array(encoding) for encoding in data["encodings"]]

# WebSocket server settings
HOST = '10.195.38.128'
PORT = 12345

# Function to process frames and encode them
def process_frame():
    # Capture a frame from the camera
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform face recognition
    face_locations = fr.face_locations(frame)
    face_encodings = fr.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
        name = "Unknown"
        if True in matches:
            best_match_index = np.argmin(fr.face_distance(known_face_encodings, face_encoding))
            name = known_face_names[best_match_index]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Label the face with a name
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    # Encode the frame as JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    return buffer.tobytes()

# WebSocket handler
async def websocket_handler(websocket):
    # print(f"WebSocket client connected: {path}")
    try:
        while True:
            # Get the processed frame
            frame_data = process_frame()
            # Send the frame data to the client
            await websocket.send(frame_data)
            await asyncio.sleep(0.03)  # ~30 FPS
    except websockets.exceptions.ConnectionClosed as e:
        print(f"WebSocket client disconnected: {e}")

# Start WebSocket server
async def start_websocket_server():
    print(f"Starting WebSocket server at {HOST}:{PORT}")
    async with websockets.serve(websocket_handler, HOST, PORT):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(start_websocket_server())
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        picam2.stop()
