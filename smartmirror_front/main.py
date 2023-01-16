import webbrowser
import sys
import os
#import ctypes
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal, QThread
from PyQt5 import QtCore,QtGui,QtWidgets,uic
from functools import partial
BASE_DIR = Path(__file__).resolve().parent

UI_class = uic.loadUiType(str(BASE_DIR) + "/desinger.ui")[0]

#QMainWindow,QWidget
#widget = QtWidgets.QStackedWidget()
class MyWindow(QtWidgets.QMainWindow, UI_class):
    def __init__(self,filesIndex,q):
        super().__init__()
        self.setupUi(self)
        self.initUI(filesIndex)
        self.customsignal = CustomSignal(q)
        self.customsignal.poped.connect(self.funcEmit)
        self.customsignal.start()
        self.show()

    def initUI(self,filesIndex):
        self.setWindowTitle("파일 오픈")
        self.exefiles = self.importfile(filesIndex)
        try:
            self.pushButton1.clicked.connect(partial(self.executeFile,exefiles[0]))
            self.pushButton2.clicked.connect(partial(self.executeFile,exefiles[1]))
            self.pushButton3.clicked.connect(partial(self.executeFile,exefiles[2]))
            self.pushButton4.clicked.connect(partial(self.executeFile,exefiles[3]))
            
        except:
            pass
        imagefiles = self.importfileImage(filesIndex)
        try:
            self.pushButton1.setStyleSheet('border-image:url('+ str(BASE_DIR).replace('\\', '/') + '/images' + str(filesIndex) + "/" + imagefiles[0] +'); border :0px;')
            self.pushButton2.setStyleSheet('border-image:url('+ str(BASE_DIR).replace('\\', '/') + '/images' + str(filesIndex) + "/" + imagefiles[1] +'); border :0px;')
            self.pushButton3.setStyleSheet('border-image:url('+ str(BASE_DIR).replace('\\', '/') + '/images' + str(filesIndex) + "/" + imagefiles[2] +'); border :0px;')
            self.pushButton4.setStyleSheet('border-image:url('+ str(BASE_DIR).replace('\\', '/') + '/images' + str(filesIndex) + "/" + imagefiles[3] +'); border :0px;')
        except:
            pass
        

    #현재 경로에 있는 exe파일 실행하는 함수
    def importfile(self, filesIndex):
        path = str(BASE_DIR) + "/exefiles" + str(filesIndex) + "/"
        file_list = os.listdir(path)
        file_list_exe = [file for file in file_list if file.endswith(".exe")]        
        return file_list_exe

    def importfileImage(self, filesIndex):
        path = str(BASE_DIR) + "/images" + str(filesIndex) + "/"
        fileImage_list = os.listdir(path)
        fileImage_list_exe = [file for file in fileImage_list if file.endswith(".png")]        
        return fileImage_list_exe

    def executeFile(self, filepath): # exe 파일 경로를 가져와서 실행
        os.system(filepath)

    @pyqtSlot(int)
    def funcEmit(self, value):
        self.executeFile(self.exefiles[0])
        if value == 0:
            self.executeFile(self.exefiles[0])
        if value == 1:
            self.executeFile(self.exefiles[1])
        if value == 2:
            self.executeFile(self.exefiles[2])
        if value == 3:
            self.executeFile(self.exefiles[3])
    # def fileopen(self):
    #     global filename
    #     filename = QtWidgets.QFileDialog.getOpenFileName(self, '')
    
    # def button1Function(self):
    #     webbrowser.open('www.naver.com')

    # def button2Function(self):
    #     os.system('"C:\windows\system32\\calc.exe"') #기본 계산기 exe 파일 경로 /  cmd.exe(도스창)을 실행하여 실행파일을 구동합니다.
    #     #calc = ("C:\windows\system32\\calc.exe") # 해당 실행 파일 경로
    #     #ctypes.windll.shell32.ShellExecuteA(0, 'open', calc, None, None, 1) #실행이 되지 않음, 하지만 이 방식이 cmd.exe를 통하지 않고 실행되며, 메모리 상으로도 Python 귀속하지 않는다.

    # def button3Function(self):
    #     webbrowser.open('"C:\windows\system32\\charmap.exe"')

    # def button4Function():
    #     webbrowser.open('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8')
    

class CustomSignal(QThread):
    poped = pyqtSignal(int)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            if not self.q.empty():
                data = self.q.get()
                self.poped.emit(data)

# if __name__=='__main__':
#     app=QtWidgets.QApplication(sys.argv)
#     customsignal = CustomSignal()
#     mywindow=MyWindow(0,customsignal)  #MyWindow의 인스턴스 생성  
#     app.exec()
    
    


