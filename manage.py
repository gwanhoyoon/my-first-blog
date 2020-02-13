#!/usr/bin/env python
import os
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        print(__name__)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    print(threading.current_thread())
    app = QApplication(sys.argv)
    a = MyMain()
    a.show()
    app.exec_()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)
    