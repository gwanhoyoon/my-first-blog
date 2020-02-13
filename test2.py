from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        print(__name__)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #a = MyMain()
    #a.show()
    #app.exec_()
