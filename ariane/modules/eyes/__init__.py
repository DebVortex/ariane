import face_recognition

import glob

from PIL import Image
from io import BytesIO

import os


class Eyes:

    def __init__(self) -> None:
        self.persons = []
        self.encodings = []
        faces_dir = os.path.dirname(os.path.abspath(__file__))
        for filePath in glob.glob(faces_dir + '/faces/*.jpg'):
            img = face_recognition.load_image_file(filePath)
            self.persons.append(filePath.split('/')[-1].replace('.jpg', ''))
            self.encodings.append(face_recognition.face_encodings(img)[0])

    def handle(self, img) -> list:
        return self._recognize_persons(img)

    def _recognize_persons(self, img) -> list:
        face_locations = face_recognition.face_locations(img)
        face_encodings = face_recognition.face_encodings(img, face_locations)
        recognized_persons = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(list(self.encodings), face_encoding)
            if matches:
                for idx, match in enumerate(matches):
                    if match:
                        recognized_persons.append(self.persons[idx])
            else:
                recognized_persons.append('')
        return recognized_persons
