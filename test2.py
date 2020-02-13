from pyqt5.QtCore import *
from pyqt5.QtWidgets import *
from pyqt5.QtGui import *
import sys
import os
import threading

class MyMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print(__name__)


if __name__ == "__main__":
    print(threading.current_thread())
    print(threading.main_thread())
    app = QApplication(sys.argv)
    a = MyMain()
    a.show()
    sys.exit(app.exec_())
