import cv2
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

class SimpleFaceRecognizer:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.known_faces = []
        self.known_names = []

    def extract_face_features(self, image_path_or_bytes):
        """Extract simple features from face using OpenCV"""
        try:
            if isinstance(image_path_or_bytes, str):
                img = cv2.imread(image_path_or_bytes)
            else:
                file_bytes = np.asarray(bytearray(image_path_or_bytes.read()), dtype=np.uint8)
                img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if img is None:
                return None

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                return None

            x, y, w, h = faces[0]
            face_roi = gray[y:y+h, x:x+w]
            face_standard = cv2.resize(face_roi, (100, 100))
            features = face_standard.flatten() / 255.0
            return features

        except Exception as e:
            print(f"Error extracting features: {e}")
            return None

    def load_known_faces(self, known_faces_dir="known_faces"):
        """Load all known faces from directory"""
        self.known_faces = []
        self.known_names = []

        if not os.path.exists(known_faces_dir):
            os.makedirs(known_faces_dir)
            return [], []

        files_in_dir = [f for f in os.listdir(known_faces_dir) 
                       if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not files_in_dir:
            return [], []

        for filename in files_in_dir:
            image_path = os.path.join(known_faces_dir, filename)
            features = self.extract_face_features(image_path)

            if features is not None:
                self.known_faces.append(features)
                name = os.path.splitext(filename)[0].replace('_', ' ').title()
                self.known_names.append(name)

        return self.known_faces, self.known_names

    def recognize_faces(self, class_photo_bytes, similarity_threshold=0.6):
        """Recognize faces in a class photo"""
        try:
            file_bytes = np.asarray(bytearray(class_photo_bytes.read()), dtype=np.uint8)
            class_img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if class_img is None:
                return [], 0, None, "Could not load class photo."

            class_img_rgb = cv2.cvtColor(class_img, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(class_img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                return [], 0, class_img_rgb, f"No faces detected in class photo."

            from PIL import Image, ImageDraw
            pil_image = Image.fromarray(class_img_rgb)
            draw = ImageDraw.Draw(pil_image)

            present_students = []
            unknown_count = 0

            for i, (x, y, w, h) in enumerate(faces):
                face_roi = gray[y:y+h, x:x+w]
                face_standard = cv2.resize(face_roi, (100, 100))
                test_features = face_standard.flatten() / 255.0

                best_similarity = 0
                best_match = "Unknown"

                for j, (known_features, name) in enumerate(zip(self.known_faces, self.known_names)):
                    try:
                        similarity = cosine_similarity([test_features], [known_features])[0][0]
                        if similarity > best_similarity and similarity > similarity_threshold:
                            best_similarity = similarity
                            best_match = name
                    except Exception as e:
                        print(f"Error comparing face with {name}: {e}")
                        continue

                if best_match != "Unknown":
                    present_students.append(best_match)
                    color = (0, 255, 0)  # Green
                else:
                    unknown_count += 1
                    color = (255, 0, 0)  # Red

                draw.rectangle([x, y, x+w, y+h], outline=color, width=3)
                draw.rectangle([x, y-25, x+w, y], fill=color)
                draw.text((x+5, y-20), best_match, fill=(255, 255, 255))

            return present_students, unknown_count, pil_image, f"Found {len(faces)} faces."

        except Exception as e:
            print(f"Error in face recognition: {e}")
            return [], 0, None, f"Error: {str(e)}"