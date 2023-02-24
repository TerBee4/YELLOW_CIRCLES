import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from random import randrange


circles = []


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.btn = QPushButton('Крух', self)
        self.btn.resize(50, 50)
        self.btn.move(400, 400)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def initUI(self):
        self.setGeometry(500, 100, 850, 850)
        self.setWindowTitle('Рисование')

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        global circles
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        a = randrange(250)
        circles.append((randrange(700), randrange(700), a, a))
        for i in circles:
            qp.drawEllipse(i[0], i[1], i[2], i[3])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())