from PyQt5.QtWidgets import QApplication
import sys
import threading

if __name__ == "__main__":
    print(threading.current_thread())
    print(threading.main_thread())
    print('============================================================')
    #app = QApplication(sys.argv)
    #a = MyMain()
    #a.show()
    #app.exec_()
