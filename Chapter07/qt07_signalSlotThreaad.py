# -*- coding: utf-8 -*-

"""
    【简介】
    多线程更新跟新数据，pyqt5界面实时刷新例子 


"""

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QMutex
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QFormLayout
import time
import sys


# mutex = QMutex()


class BackendThread1(QThread):
    # 通过类成员对象定义信号对象  
    update_date = pyqtSignal(str)

    # 处理要做的业务逻辑
    def run(self):
        while True:
            x = int(time.strftime("%Y%m%d%H%M%S", time.localtime())[-2:-1])
            try:
                print("1=", (x % 2) != 0, "\n")
                if (x % 2) != 0:
                    data = QDateTime.currentDateTime()
                    currTime = data.toString("yyyy-MM-dd *1* hh:mm:ss")
                    self.update_date.emit(str(currTime))
                    # mutex.lock()
                # else:

            except Exception as e:
                print("e=", e)

            # mutex.unlock()
            time.sleep(1)


class BackendThread2(QThread):
    # 通过类成员对象定义信号对象
    update_date = pyqtSignal(str)

    # 处理要做的业务逻辑
    def run(self):
        while True:
            try:
                x = int(time.strftime("%Y%m%d%H%M%S", time.localtime())[-2:-1])
                print("2=", (x % 2) == 0, "\n")
                if (x % 2) == 0:
                    data = QDateTime.currentDateTime()
                    currTime = data.toString("yyyy-MM-dd *2* hh:mm:ss")
                    self.update_date.emit(str(currTime))
                    # mutex.lock()
                # else:

            except Exception as e:
                print("e=", e)

            # mutex.unlock()
            time.sleep(1)


class Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('pyqt5界面实时更新例子')

        flo = QFormLayout()
        self.resize(600, 600)

        self.input1 = QLineEdit(self)
        self.input1.resize(200, 100)

        self.input2 = QLineEdit(self)
        self.input2.resize(200, 100)

        self.input3 = QLineEdit(self)
        self.input3.resize(200, 100)

        flo.addRow("input1", self.input1)
        flo.addRow("input2", self.input2)
        flo.addRow("input3", self.input3)
        self.setLayout(flo)

        self.initUI()

    def initUI(self):
        # 创建线程  
        self.backend1 = BackendThread1()
        # 连接信号 
        self.backend1.update_date.connect(self.handleDisplay1)
        # 开始线程  
        self.backend1.start()

        self.backend2 = BackendThread2()
        # 连接信号
        self.backend2.update_date.connect(self.handleDisplay2)
        # 开始线程
        self.backend2.start()

    def seconds_judge(self, ):
        x = (time.strftime("%Y%m%d%H%M%S", time.localtime())[-2:-1])
        if x % 2 == 0:
            return True
        else:
            return False

    # 将当前时间输出到文本框
    def handleDisplay1(self, data):
        self.input1.setText(data)
        # if self.seconds_judge():
        # self.input3.setText(data)

    def handleDisplay2(self, data):
        self.input2.setText(data)
        self.input3.setText(data)


"""
一会儿显示1 一会儿显示2   不冲突  怎么巧妙的设计一下
60秒
10 - 30  50  1显示 
20 - 40  60  2显示


"""

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("e=", e)
