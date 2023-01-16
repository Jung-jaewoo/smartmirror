from multiprocessing import Process, Queue
from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
import time
from multiprocessing import Process, Pipe
from smartmirror_front import main
import smartmirror_back.cam as cam


def makeNewThread(procnum, mywindow, q):
    app=QtWidgets.QApplication(sys.argv)
    mywindow=main.MyWindow(procnum, q)     
    app.exec()


if __name__ == "__main__":
    action = 0
    mywindow = None
    procnum = 0

    th1 = Process(target=makeNewThread, args=(procnum, mywindow, cam.q))
    th1.start()

    cam.startCam()
    
