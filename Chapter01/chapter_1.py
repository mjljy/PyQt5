# -*- coding: utf-8 -*-


"""
认识PyQt5
PyQt5是Qt所有类的pyhton封装，也就是说本质上还是Qt，那么Qt是什么呢？
https://github.com/cxinping/PyQt5
这个一个客户端的框架系统，也就是说 框架已经做好了 不需要你在徒手做一个框架
现在要做的就是  学习、理解、掌握、应用这个框架
怎么理解这个框架呢？
qt使用一种称为 信号/槽 的机制在窗口控件之间传递事件和消息，完全同于其他图形界面开发库 所采用的回调机制
这样更安全和简洁


QtDesigner、pyqt5-tools图形界面的开发工具

QtWidgets

QtCore


在线文档


https://maicss.com/pyqt/v6/
https://www.tutorialspoint.com/pyqt5/index.htm
https://www.pythonguis.com/
https://doc.qt.io/qtforpython-5/



"""

import sys
from PyQt5 import QtWidgets, QtCore

# QtWidgets 元素空间
# QtCore 非GUI核心


def demo1():
    #
    app = QtWidgets.QApplication(sys.argv)
    #
    widget = QtWidgets.QWidget()
    # 设置大小尺寸
    widget.resize(180, 360)
    # 标题
    widget.setWindowTitle("hello,pyqt5")
    # 展示
    widget.show()
    # 退出
    # sys.exit()函数可以结束一个应用程序，使应用程序在主循环中退出
    sys.exit(app.exec_())


if __name__ == "__main__":
    demo1()
