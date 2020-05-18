from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide2.QtWidgets import QSizePolicy, QFrame, QSizePolicy
from PySide2 import QtCore, QtGui


class Image(QLabel):
    def __init__(self, path=None):
        super(Image, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(path)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

    def paintEvent(self, event):
        if self.pixmap == self.pixmap:
            size = self.size()
            painter = QtGui.QPainter(self)
            point = QtCore.QPoint(0,0)
            scaledPix = self.pixmap.scaled(size,
                                        QtCore.Qt.KeepAspectRatio,
                                        transformMode = QtCore.Qt.SmoothTransformation)
            point.setX((size.width() - scaledPix.width()) / 2)
            point.setY((size.height() - scaledPix.height()) / 2)
            painter.drawPixmap(point, scaledPix)

    def setImage(self, path):
        self.pixmap = QtGui.QPixmap(path)
        self.repaint()

    def clear(self):
        pass
        # solve it later
        # self.pixmap = None
        # self.repaint()

class ImageFrame(QWidget):
    def __init__(self, background=None):
        super(ImageFrame, self).__init__()
        self.image = Image()

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.image)
        self.setStyleSheet(background)
        self.setLayout(verticalLayout)

    def setImage(self, path):
        self.image.setImage(path)

    def clear(self):
        self.image.clear()
