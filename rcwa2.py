# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import threading
import sys

class MyMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        print(__name__)
        
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
    app = QApplication(sys.argv)
    print(threading.current_thread())
    print(threading.main_thread())
    a = MyMain()
    a.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    #a = MyMain()
    #a.show()
    #sys.exit(app.exec_())