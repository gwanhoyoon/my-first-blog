#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
import PyQt5
import numpy
import matplotlib
import sys
import os
import threading

class MyMain(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print(__name__)

if __name__ == "__main__":
    print(threading.current_thread())
    print(threading.main_thread())
    app = PyQt5.QtGui.QApplication(sys.argv)
    #a = MyMain()
    #a.show()
    #sys.exit(app.exec_())
