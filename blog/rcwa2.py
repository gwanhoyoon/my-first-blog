from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import re

class MyMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        self.setGeometry(700, 400, 200, 100)
        img = QLabel()
        pixmap = QPixmap('images\\batman.png')
        img.setPixmap(pixmap)
        img.resize(pixmap.width(),pixmap.height())
        layout = QVBoxLayout()
        layout.addWidget(img)
        self.setLayout(layout)
        