import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 500, 500)
        self.setMaximumSize(500, 500)
        self.setMinimumSize(500, 500)
        self.pix = QPixmap('files/ufo.jpg')
        self.img = QtWidgets.QLabel(self)
        self.img.setGeometry(0, 0, 50, 50)
        self.img.setPixmap(self.pix)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.img.setGeometry(self.img.x(), self.img.y() + 10, 50, 50)
        if event.key() == Qt.Key_Up:
            self.img.setGeometry(self.img.x(), self.img.y() - 10, 50, 50)
        if event.key() == Qt.Key_Right:
            self.img.setGeometry(self.img.x() + 10, self.img.y(), 50, 50)
        if event.key() == Qt.Key_Left:
            self.img.setGeometry(self.img.x() - 10, self.img.y(), 50, 50)
        if self.img.x() < 0:
            self.img.setGeometry(450, self.img.y(), 50, 50)
        if self.img.x() + 50 > 500:
            self.img.setGeometry(0, self.img.y(), 50, 50)
        if self.img.y() < 0:
            self.img.setGeometry(self.img.x(), 450, 50, 50)
        if self.img.y() + 50 > 500:
            self.img.setGeometry(self.img.x(), 0, 50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec())