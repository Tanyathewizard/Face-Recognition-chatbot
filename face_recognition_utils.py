# Import necessary libraries
import os
import face_recognition
import cv2  # needed for BGR to RGB conversion

# Function to load known face images and extract face encodings

def load_known_faces(folder=None):
    if folder is None:
        folder = os.path.join(os.path.dirname(__file__), "known_faces")
     


    if not os.path.exists(folder):
        print(f"Creating folder: {folder}")
        os.makedirs(folder)
        return [], []

    known_encodings = [] # Stores face encodings
    known_names = [] # Stores corresponding names

    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        
            image_path = os.path.join(folder, filename)

            # Load with OpenCV and convert BGR to RGB
            bgr_image = cv2.imread(image_path)
            if bgr_image is None:
                print(f"Error loading image: {filename}")
                continue

            rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
                
            # Get the face encodings from the image
            encodings = face_recognition.face_encodings(rgb_image)
            if encodings:
                known_encodings.append(encodings[0]) 
                name = os.path.splitext(filename)[0]
                known_names.append(name.lower())
            else:
                print(f"No face found in {filename}. Skipping.")

    return known_encodings, known_names

# Compare the captured face to known encodings and return matched name (if any)
def recognize_user(image_path, known_encodings, known_names, tolerance=0.5):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if not encodings:
        print("No face detected in captured image.")
        return None

    captured_encoding = encodings[0]
    matches = face_recognition.compare_faces(known_encodings, captured_encoding, tolerance)

    for idx, match in enumerate(matches):
        if match:
            return known_names[idx]

    return None
