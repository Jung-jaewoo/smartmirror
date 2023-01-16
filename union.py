from multiprocessing import Process, Queue
from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
import time
from multiprocessing import Process, Pipe
from smartmirror_front import main
import smartmirror_back.cam as cam
import multiprocessing as mp
import datetime

def makeNewThread(procnum, mywindow):
    q = Queue()
    p = Process(name="produce", target=producer, args=(q, ), daemon=True)
    p.start()    
    app=QtWidgets.QApplication(sys.argv)
    mywindow=main.MyWindow(procnum, q)     
    app.exec()

def producer(q):
    proc = mp.current_process()
    print(proc.name)

    while True:
        now = datetime.datetime.now()
        data = str(now)
        q.put(data)
        time.sleep(1)

if __name__ == "__main__":
    action = 0
    mywindow = None
    procnum = 0

    th1 = Process(target=makeNewThread, args=(procnum, mywindow))
    th1.start()

    # cam.startCam()
    
