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


def camthread(procnum, result1):
    cam.startCam()  


result1, result2 = Pipe()
if __name__ == "__main__":
    mywindow = None
    procnum = 1
    procnum2 = 2
    th1 = Process(target=mainthread, args=(procnum, mywindow))
    th2 = Process(target=camthread, args=(procnum2, result1))
    th1.start()
    th2.start()
    while True:
        print("받았다!@ :" + str(result2.recv()))

    th1.join()
    th2.join()
    