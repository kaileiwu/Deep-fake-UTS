import numpy as np
import cv2
import os

from model.face_detector import FaceDetector
from model.vgg19 import VGG19
model = VGG19()
fd = FaceDetector()

def process(path):
    image = cv2.imread(path)
    faces_coord = fd.detect_faces(image)
    print('faces_coord %i' % (len(faces_coord)))
    
    faces=[]
    for rec in faces_coord:
        face_img = image[rec[1]:rec[1]+rec[2], rec[0]:rec[0]+rec[2]]
        face_img_resized = cv2.resize(face_img, (224, 224), interpolation = cv2.INTER_AREA)
        faces.append((rec, model.model.predict(np.asarray([face_img_resized]))))
    
    rect_faces = fd.draw_rects(image, faces)

    filename = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(filename, './out/out.jpg')
    cv2.imwrite(filename, rect_faces)
    return filename