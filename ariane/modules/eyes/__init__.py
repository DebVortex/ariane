import os
import glob
import logging

import face_recognition

from PIL import Image
from io import BytesIO


class Eyes:

    def __init__(self) -> None:
        """ Initialize the eyes module.
        
        Loads the face files and create the related encodings.
        """
        print("INFO: Initializing eyes")
        self.persons = []
        self.encodings = []
        faces_dir = os.path.dirname(os.path.abspath(__file__))
        for filePath in glob.glob(faces_dir + '/faces/*.jpg'):
            print(f"INFO: Loading face from {filePath}")
            img = face_recognition.load_image_file(filePath)
            person = filePath.split('/')[-1].replace('.jpg', '')
            print(f"INFO: Found face for {person}. Adding to persons and encodings.")
            self.persons.append(person)
            self.encodings.append(face_recognition.face_encodings(img)[0])
        print("INFO: Done initializing eyes")

    def handle(self, img) -> list:
        """ Handle the given image.
        
        Returns a list of recognized persons."""
        return self._recognize_persons(img)

    def _recognize_persons(self, img) -> list:
        """ Recognize the persons in the given image. """
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
