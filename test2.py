from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import threading

def main():
    print(threading.current_thread())
    print(threading.main_thread())

if __name__ == "__main__":
    main()
