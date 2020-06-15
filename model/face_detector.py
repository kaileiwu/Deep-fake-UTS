import pip
import os
import cv2

class FaceDetector:
    RECT_SCALE = 1
    def __init__(self):
        self.import_or_install('mtcnn')
        self.detector = None
        try:
            from mtcnn.mtcnn import MTCNN
            self.detector = MTCNN()
        except ImportError:
            print('\nCannot import MTCNN\n')
        
    def import_or_install(self, package):
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])

    def detect_faces(self, image):
        face_coords=[]

        faces = self.detector.detect_faces(image)
        # print('Number of recognised faces %i' % len(faces))
        for face in faces:
            x, y, width, height = face['box']

            new_width = self.RECT_SCALE * width
            new_height = self.RECT_SCALE * height
            
            side = int(new_width if new_width > new_height else new_height)

            x = x - int((side - width) / 2)
            y = y - int((side - height) / 2)
            
            face_coords.append((x, y, side))
        return face_coords
    
    def draw_rects(self, image, pred_faces):
        out = image
        for face in pred_faces:
            color = (0, 0, 0)
            if face[1] > 0.5:
                # print('REAL')
                color = (0, 255, 0)
            else:
                # print('FAKE')
                color = (255, 0, 0)

            x1 = face[0][0]
            y1 = face[0][1]
            x2 = face[0][0]+face[0][2]
            y2 = face[0][1]+face[0][2]
            out = cv2.rectangle(out, (x1, y1), (x2, y2), color, thickness=3)
        
        return out