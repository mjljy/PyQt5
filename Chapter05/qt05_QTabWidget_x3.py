# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class QTalbeWidget_test(QTableWidget):
    def __init__(self):
        super().__init__()
        # 设置 左上角的标题
        self.setWindowTitle("special")
        # 设置窗口图标
        # 设置图标的图片
        self.setWindowIcon(QIcon("icon.png"))
        # 设置大小
        self.resize(600, 200)
        # 设置列
        self.setColumnCount(3)
        # 设置行
        self.setRowCount(6)
        # 设置焦点方式
        # https://blog.csdn.net/jays_/article/details/83783871
        # 不能通过上两种方式获得焦点(默认值),setFocus仍可使其获得焦点.
        self.setFocusPolicy(Qt.NoFocus)
        # setHorizontalHeaderLabels  设置QTableWidget表格控件的水平标签
        # self.setHorizontalHeaderLabels(self.column_name)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    myTable = QTalbeWidget_test()
    myTable.show()
    sys.exit(app.exec_())
