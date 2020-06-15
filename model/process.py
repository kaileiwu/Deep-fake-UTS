import numpy as np
import cv2
import os

from model.face_detector import FaceDetector
from model.vgg19 import VGG19
trained_model = VGG19()
face_detector = FaceDetector()

def process(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    faces_coord = face_detector.detect_faces(image)
    
    faces=[]
    for rec in faces_coord:
        face_img = image[rec[1]:rec[1]+rec[2], rec[0]:rec[0]+rec[2]]
        face_img_resized = cv2.resize(face_img, (224, 224), interpolation = cv2.INTER_AREA)

        # Predict fake or real, 1 - real, 0 - fake
        pred = trained_model.model.predict(np.asarray([face_img_resized]))
        face_pred = (rec, pred)

        faces.append(face_pred)
    
    rect_faces = face_detector.draw_rects(image, faces)

    filename = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(filename, './out/out.jpg')

    rect_faces = cv2.cvtColor(rect_faces, cv2.COLOR_BGR2RGB)
    cv2.imwrite(filename, rect_faces)

    return filename