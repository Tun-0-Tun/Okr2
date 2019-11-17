import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import Qt
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMouseTracking(True)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('поменять', self)
        self.btn.resize(100, 50)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.DrawFl)

        self.show()
        self.a = 1
        self.fl = False
        self.status = 0



    def DrawFl(self):
        self.fl = True
        self.update()

    def paintEvent(self, event):
        if self.fl:
            print('gg')
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawFlag()
            self.qp.end()


    def drawFlag(self):
        self.qp.setBrush(QColor(randint(200, 250), randint(200, 250),  randint(200, 250)))
        self.qp.drawEllipse(50, 50, randint(50, 250), randint(50, 250))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
