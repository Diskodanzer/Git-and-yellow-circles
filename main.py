import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QPen
import random
from PyQt6.QtCore import Qt



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)
        self.circles = []
        self.pushButton.clicked.connect(self.generate)
    
    def generate(self):
        self.circles = [random.randint(10, 100) for _ in range(random.randint(2, 9))]
        self.update()
    
    def paintEvent(self, a0):
        p = QPainter(self)
        pen = QPen(Qt.GlobalColor.yellow, 3)
        p.setPen(pen)
        for elem in self.circles:
            p.drawEllipse(random.randint(0, 800), random.randint(0, 600), elem, elem)
        self.circles = []
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mn = Main()
    mn.show()
    sys.exit(app.exec())