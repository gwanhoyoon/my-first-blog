from PyQt5.QtWidgets import QApplication
import sys
import threading
import numpy

if __name__ == "__main__":
    print(threading.current_thread())
    print(threading.main_thread())
    print('============================================================')
    a = numpy.array([[1,2],[3,4]])
    b = numpy.array([[1,2],[3,4]])
    c = a+b
    print(c)
    #app = QApplication(sys.argv)
    #a = MyMain()
    #a.show()
    #app.exec_()
