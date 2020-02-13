# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os

class MyMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        print(__name__)
        print('Hi!!!!')
        
    def setupUI(self):
        self.setGeometry(700, 400, 200, 100)
        img = QLabel()
        pixmap = QPixmap('images\\batman.png')
        img.setPixmap(pixmap)
        img.resize(pixmap.width(),pixmap.height())
        layout = QVBoxLayout()
        layout.addWidget(img)
        self.setLayout(layout)

def main():
    #app = QApplication(sys.argv)
    #a = MyMain()
    #a.show()
    #sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    #a = MyMain()
    #a.show()
    #sys.exit(app.exec_())