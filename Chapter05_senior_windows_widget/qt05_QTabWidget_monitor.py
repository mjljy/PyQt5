#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:admin
# datetime:2025/6/3 13:46
# software: PyCharm
# brief :
import  sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QHeaderView, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MyTable(QTableWidget):
    def __init__(self, parent=None, table_name='表格名称', column_name=['A', 'B', 'C'],
                 row_name=['row1', 'row2', 'row3'], table_order=1):
        """

        :param parent:
        :param table_name:
        :param column_name:
        :param row_name:
        :param table_order:
        """
        super(MyTable, self).__init__(parent)
        self.table_order = table_order # 一个判断条件  后续用
        self.setWindowTitle(table_name) # 标题名称

        # 划表格行列数
        self.setColumnCount(len(column_name)) # 列数
        self.setRowCount(len(row_name))  # 行数

        # 设置  不获得焦点
        self.setFocusPolicy(Qt.NoFocus) # 不能通过上两种方式获得焦点(默认值),setFocus仍可使其获得焦点.

        # 设置画的行列表格的 列明和行名
        self.column_name = column_name  # 列明
        self.row_name = row_name        # 行名
        # 创建表头的最简单方法是向setHorizontalHeaderLabels() 和setVerticalHeaderLabels() 函数提供字符串列表
        self.setHorizontalHeaderLabels(self.column_name)
        # 将column 列的水平标题项目设置为item 。如有必要，将增加列数以适应该项目。之前的页眉项（如果有的话）将被删除
        # 将row 行的垂直标题项设置为item 。
        self.setVerticalHeaderLabels(self.row_name)
        # 设置水平方向上的名字

        #
        # https://blog.csdn.net/ffffffeiyu/article/details/136374246
        # setSectionResizeMode 函数在 Qt 库中用于设置 QHeaderView 或类似类（如 QTableWidgetHeader、QTreeViewHeader）的某一列或某一行的自动调整模式
        # - QHeaderView.ResizeToContents: 列宽根据内容自动调整
        # - QHeaderView.ResizeToContents: （仅限旧版，与 ResizeToContents 相同
        #
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 表格宽度的自适应调整
        #
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # https://doc.qt.io/qt-6/zh/stylesheet-examples.html
        # Qt 样式表示例
        self.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #f0f0f0;        # 元素的背景颜色
                border-bottom: 2px solid black;   # border-bottom  用于设置下边框宽度、样式和颜色的速记符号
            }
        """)
        font = QFont()
        # 将字体大小设置为pixelSize 像素，最大字体大小为无符号 16 位整数。
        font.setPointSize(8)
        # 将字体大小设置为pixelSize 像素，最大字体大小为无符号 16 位整数。
        self.setFont(font)


class MainWindow(QWidget):
    """
        创建一个主窗口、创建tab、初始化n个table、表格放入tab、创建数据更新线程、连接信号槽
    """
    def __init__(self,table1,table2):
        super(MainWindow, self).__init__()
        self.setWindowTitle("弈倍盘中实时风控检测系统")
        # self.setWindowIcon(QIcon("qfund/view/ok.png"))
        self.showMaximized()

        self.tab_widget = QTabWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tab_widget)

        self.table1 = table1
        self.table2 = table2

        self.tab_widget.addTab(self.table1, "账户")
        self.tab_widget.addTab(self.table2, "产品")

        # self.update_data_thread1 = UpdateData()
        # self.update_data_thread2 = UpdateData()
        #
        # self.update_data_thread1.update_date.connect(self.table1.update_item_data)
        # self.update_data_thread2.update_date.connect(self.table2.update_item_data)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    table1 = MyTable(table_name='表格1', column_name=[f"A{i}" for i in range(1, 21)],
                     row_name=[f"B{i}" for i in range(1, 21)], table_order=1)

    table2 = MyTable(table_name='表格2', column_name=[f"A{i}" for i in range(1, 21)],
                     row_name=[f"B{i}" for i in range(1, 21)],table_order=2)



    main_window = MainWindow(table1,table2)
    main_window.show()

    sys.exit(app.exec_())
