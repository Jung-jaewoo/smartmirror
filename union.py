from multiprocessing import Process, Queue
from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
from smartmirror_front import main
# from smartmirror_back import cam


def mainthread(procnum, mywindow):
    app=QtWidgets.QApplication(sys.argv)
    mywindow=main.MyWindow()     
    app.exec()

def camthread(procnum, result):
    from smartmirror_back import cam
    result = 1

if __name__ == "__main__":
    mywindow = None
    procnum = 1
    procnum2 = 2
    result = None
    th1 = Process(target=mainthread, args=(procnum, mywindow))
    th2 = Process(target=camthread, args=(procnum2, result))
    th1.start()
    th2.start()
    th1.join()
    th2.join()