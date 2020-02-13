import sys
import os
import threading

def main():
    app = QApplication(sys.argv)
    print(threading.current_thread())
    print(threading.main_thread())

if __name__ == "__main__":
    main()
