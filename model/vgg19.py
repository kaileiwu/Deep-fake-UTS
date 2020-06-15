
from keras import models
import numpy as np
import os

class VGG19:
    def __init__(self):
        super().__init__()
        path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(path, './weights/weights.14-0.08.hdf5')
        self.model = models.load_model(path)

    def predict(self, face):
        return self.model.predict(face)
