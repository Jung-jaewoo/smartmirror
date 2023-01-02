from multiprocessing import Process, Queue
from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
import time
from multiprocessing import Process, Pipe
from smartmirror_front import main
import smartmirror_back.cam as cam

def mainthread(procnum, mywindow):
    app=QtWidgets.QApplication(sys.argv)
    mywindow=main.MyWindow()     
    app.exec()


result1, result2 = Pipe()
if __name__ == "__main__":
    mywindow = None
    procnum = 1
    procnum2 = 2
    th1 = Process(target=mainthread, args=(procnum, mywindow))
    th1.start()
    cam.startCam()
    print(1)
    