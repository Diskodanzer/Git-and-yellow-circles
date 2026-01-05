import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen
import random

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.colors = [
            Qt.GlobalColor.red,
            Qt.GlobalColor.green, 
            Qt.GlobalColor.blue,
            Qt.GlobalColor.yellow,
            Qt.GlobalColor.magenta,
            Qt.GlobalColor.cyan,
            Qt.GlobalColor.white,
            Qt.GlobalColor.black,
            Qt.GlobalColor.gray
        ]
    
    def generate(self):
        self.circles = [random.randint(10, 100) for _ in range(random.randint(2, 9))]
        self.update()
        
    def setup_ui(self):
        self.setGeometry(0, 0, 800, 600)
        self.pushButton = QPushButton("сгенерировать", self)
        self.pushButton.move(20, 20)
        self.pushButton.clicked.connect(self.generate)
    
    def paintEvent(self, a0):
        p = QPainter(self)
        pen = QPen(random.choice(self.colors), 3)
        p.setPen(pen)
        for elem in self.circles:
            p.drawEllipse(random.randint(0, 800), random.randint(0, 600), elem, elem)
        self.circles = []