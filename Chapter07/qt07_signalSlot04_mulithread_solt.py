# -*- coding: utf-8 -*-

"""
    【简介】
    多线程信号槽通信示例


"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # 创建一个线程实例并设置名称、变量、信号槽
        self.thread = MyThread()
        self.thread.setIdentity("thread0")
        self.thread.sinOut.connect(self.outText)
        self.thread.setVal(100)

        self.thread1 = MyThread()
        self.thread1.setIdentity("thread1")
        self.thread1.sinOut.connect(self.outText)
        self.thread1.setVal(100)

    def outText(self, text):
        print(text)


class MyThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        self.identity = None

    def setIdentity(self, text):
        self.identity = text

    def setVal(self, val):
        self.times = int(val)
        #执行线程的run方法
        self.start()

    def run(self):
        while self.times > 0 and self.identity:
            # 发射信号
            print("tag0")
            self.sinOut.emit(self.identity + "==>" + str(self.times))
            self.times -= 1
            # try:
            time.sleep(5)
            # except Exception as e:
            #     print("e=",e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
