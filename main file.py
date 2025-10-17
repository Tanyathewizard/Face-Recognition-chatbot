from camera_utils import ask_camera_permission, capture_photo, show_detected_face
from face_recognition_utils import load_known_faces, recognize_user
import os
import shutil
import json
import re
import random
from intent_bot import start_chatbot

# Step 1: Ask for permission
if not ask_camera_permission():
    print("Camera permission denied. Exiting.")
    exit()

# Step 2: Capture user face
image_path = capture_photo("captured_face.jpg")
if not image_path:
    print("Face capture failed. Exiting.")
    exit()

# Optional: Show face with green rectangle
show_detected_face(image_path)

# Step 3: Load known faces and try to match
known_encodings, known_names = load_known_faces()
matched_name = recognize_user(image_path, known_encodings, known_names)

# Step 4: If not matched, deny access
if not matched_name:
    print("Unknown face detected. Access denied.")
    exit()

# Step 5: If matched
print(f"Hello, {matched_name.capitalize()}! You are recognized.")

# Step 6: If the matched user is admin, ask to register a new user
if matched_name == "admin":
    response = input("Do you want to register a new member? (yes/no): ").strip().lower()
    if response == "yes":
        print("Starting registration for a new member...")

        # Capture new member's face
        new_image_path = capture_photo("new_member.jpg")
        if not new_image_path:
            print("New member face capture failed.")
            exit()

        show_detected_face(new_image_path)

        # Ask user details
        new_name = input("Enter the new person's name: ").strip().lower()
        department = input("Enter department: ").strip()
        purpose = input("Enter purpose of visit: ").strip()

        # Save image to known_faces/
        known_faces_dir = os.path.join(os.path.dirname(__file__), "known_faces")
        if not os.path.exists(known_faces_dir):
            os.makedirs(known_faces_dir)

        final_image_path = os.path.join(known_faces_dir, f"{new_name}.jpg")
        shutil.move(new_image_path, final_image_path)
        print(f"Saved new face as: {final_image_path}")

        # Save user info to JSON file
        user_info = {
            "name": new_name,
            "department": department,
            "purpose": purpose
        }

        json_file = os.path.join(os.path.dirname(__file__), "user_data.json")
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(user_info)
        with open(json_file, "w") as f:
            json.dump(data, f, indent=4)

        print(f"New member '{new_name}' registered successfully.")
    else:
        print("No new member registered.")

  
 
if matched_name:
    
    start_chatbot(matched_name)

    