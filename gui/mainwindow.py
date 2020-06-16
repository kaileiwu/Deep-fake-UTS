# pip3 install PySide2

from PySide2.QtWidgets import QPushButton, QLabel, QSpacerItem
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QFileDialog, QSizePolicy, QFrame
from PySide2.QtWidgets import QMainWindow, QWidget, QMenuBar

from PySide2 import QtCore, QtGui

from os import path

# nearest modules
from gui.image import Image, ImageFrame
from model.process import process

class MainWindow(QMainWindow):
    WIDTH = 800
    HEIGHT = 400
    MIN_WIDGET_SIZE = 22
    MIN_APP_WIDTH = 220
    BUTTON_HEIGHT = 34
    BUTTON_WIDTH = 90

    ORANGE_COLOR = "color: rgb(255, 153, 0);"
    BACKGROUND_COLOR = "background-color: rgb(43, 45, 53);"

    # shows selectable files in QFileDialog
    fileFilter = 'Images (*.png *.jpg *.jpeg *.tif)'
    
    def __init__(self, pyqt_app, parent=None):
        super(MainWindow, self).__init__()
        self.pyqt_app = pyqt_app
        self.currentImagePath = None

        # GUI definition
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.openFileButton = QPushButton(self.centralWidget)
        self.openFileButton.setObjectName("openFileButton")
        self.verticalLayout.addWidget(self.openFileButton)

        self.processFileButton = QPushButton(self.centralWidget)
        self.processFileButton.setObjectName("processFileButton")
        self.verticalLayout.addWidget(self.processFileButton)

        self.clearViewButton = QPushButton(self.centralWidget)
        self.clearViewButton.setObjectName("clearViewButton")
        self.verticalLayout.addWidget(self.clearViewButton)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer)

        self.imageFrame = ImageFrame(background=self.BACKGROUND_COLOR)
        self.centralWidget.setStyleSheet(self.BACKGROUND_COLOR)
        self.horizontalLayout.addWidget(self.imageFrame)

        # description of all Widgets above:
        self.setupUi()
        
        # delete Window on close button
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    
    def setupUi(self):
        # sizes and constraints
        self.resize(self.WIDTH, self.HEIGHT)

        # hardcoded, don't remember better solution
        # but works for sure, ha-ha
        self.openFileButton.setMinimumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.openFileButton.setMaximumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))

        self.processFileButton.setMinimumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.processFileButton.setMaximumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))

        self.clearViewButton.setMinimumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.clearViewButton.setMaximumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))

        self.setupConnections()
        self.retranslateUI()
        self.retranslateUIStyleSheet()
    
    # Change text var if needed:
    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.setWindowTitle(_translate("MainWindow", "DeepFake detector"))
        self.openFileButton.setText(_translate("MainWindow", "Open File"))
        self.processFileButton.setText(_translate("MainWindow", "Process"))
        self.clearViewButton.setText(_translate("MainWindow", "Clear"))
    
    # Custom palette if needed:
    def retranslateUIStyleSheet(self):
        self.openFileButton.setStyleSheet(self.ORANGE_COLOR)
        self.processFileButton.setStyleSheet(self.ORANGE_COLOR)
        self.clearViewButton.setStyleSheet(self.ORANGE_COLOR)

    def setupConnections(self):
        self.openFileButton.clicked.connect(self.onClickOpenFileButton)
        self.processFileButton.clicked.connect(self.onClickProcessFileButton)
        self.clearViewButton.clicked.connect(self.onClickClearViewButton)

    def onClickOpenFileButton(self):
        fileDialog = QFileDialog()
        fileDialog.setNameFilters(self.fileFilter)
        fileDialog.selectNameFilter(self.fileFilter)
        fileName = fileDialog.getOpenFileName(self,
                                              'Media Browser',
                                              filter=self.fileFilter)
        if fileName[0] and path.exists(fileName[0]):
            # do something with the file
            self.imageFrame.setImage(fileName[0])
            # Also, assign your image here, right now there is a path
            self.currentImagePath = fileName[0]

    def onClickProcessFileButton(self):
        if self.currentImagePath:
            self.imageFrame.setImage(process(self.currentImagePath))
            return
        print("No image to process")

    def onClickClearViewButton(self):
        self.imageFrame.clear()
        self.currentImagePath = None

    def run(self):
        self.show()
        self.pyqt_app.exec_()