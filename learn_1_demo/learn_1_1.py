#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:admin
# datetime:2025/5/29 13:56
# software: PyCharm
# brief :
"""
https://baijiahao.baidu.com/s?id=1821632563687234445&wfr=spider&for=pc


"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建一个窗口
window = QWidget()
window.setWindowTitle("PyQt5 示例")
window.setGeometry(100, 100, 300, 300)  # 设置窗口的位置和大小 (x,y, width, height)

# 创建一个标签
label = QLabel("Hello PyQt5!", parent=window)
# lable.setGeometry(100, 100, 100, 100)
label.move(100, 100)

# lable.movie(35, 40)

def button_clicked(self):
    print("按钮被点击了!")


button = QPushButton("点击我", parent=window)
# button.setGeometry(100, 100, 100, 100)
button.move(150, 150)
# button.clicked.connect(button_clicked)
button.clicked.connect(lambda :print("按钮被点击了!"))

# 显示窗口
window.show()

# 运行应用程序
sys.exit(app.exec_())
