import face_recognition
import cv2

class FaceRecognition:
    def __init__(self):
        self.face_recognizer = face_recognition.FaceRecognizer()

    def train_model(self, images, labels):
        self.face_recognizer.train(images, labels)

    def recognize_face(self, image):
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = self.face_recognizer.compare_faces(face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = self.face_recognizer.known_face_names[first_match_index]
            face_names.append(name)
        return face_names

    def draw_rectangles(self, image, face_locations, face_names):
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return image
