from sys import argv
from PySide2.QtWidgets import QApplication
import gui.mainwindow

if __name__ == '__main__':
    pyqt_app = QApplication(argv)
    gui.mainwindow.MainWindow(pyqt_app).run()