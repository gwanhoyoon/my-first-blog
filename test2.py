#from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5.QtGui import *
import sys
import threading

class MyMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print(__name__)

app = QApplication(sys.argv)
a = MyMain()
a.show()
sys.exit(app.exec_())

#if __name__ == "__main__":
#    print(threading.current_thread())
#    print(threading.main_thread())
#    app = QApplication(sys.argv)
#    a = MyMain()
#    a.show()
#    sys.exit(app.exec_())
