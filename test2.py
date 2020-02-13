#from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5.QtGui import *
import sys

class MyMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print(__name__)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MyMain()
    a.show()
    sys.exit(app.exec_())
