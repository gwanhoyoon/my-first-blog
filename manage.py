#!/usr/bin/env python
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(__name__)
    a = MyMain()
    a.show()
    sys.exit(app.exec_())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)