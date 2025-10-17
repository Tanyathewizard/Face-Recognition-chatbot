import cv2
import os

# Ask the user for camera access permission
def ask_camera_permission():
    response = input("Do you allow camera access for facial recognition? (yes/no): ").strip().lower()
    return response == "yes"

# Capture a photo from the webcam and save it
def capture_photo(temp_image_name="temp_face.jpg"):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access the camera. Check privacy settings or close other apps.")
        return None

    print("Press SPACE to capture your face or ESC to cancel.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from camera.")
            break

        cv2.imshow("Live Camera - Press SPACE to Capture", frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:
            print("Capture cancelled.")
            break
        elif key % 256 == 32:
            cv2.imwrite(temp_image_name, frame)
            print(f"Face captured and saved as: {temp_image_name}")
            cap.release()
            cv2.destroyAllWindows()
            return temp_image_name

    cap.release()
    cv2.destroyAllWindows()
    return None

# Show the captured image and highlight detected face(s)
def show_detected_face(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image '{image_path}' not found.")
        return False

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        print("No face detected in the image.")
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Detected Face", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True