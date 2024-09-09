# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个 QVBoxLayout 实例
        layout = QVBoxLayout()

        # 创建一个 QPushButton 实例，并设置其显示文本
        self.btn = QPushButton('点击我', self)
        # 连接按钮的 clicked 信号到自定义的槽函数 on_click
        self.btn.clicked.connect(self.on_click)

        # 将按钮添加到布局中
        layout.addWidget(self.btn)

        # 设置窗口的布局为我们刚刚创建的布局
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 Demo')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_click(self):
        # 当按钮被点击时执行的函数
        print('按钮被点击了！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DemoApp()
    sys.exit(app.exec_())
