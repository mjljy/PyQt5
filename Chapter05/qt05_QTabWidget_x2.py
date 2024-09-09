# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget,QWidget


class QTalbeWidget_test(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("special")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myTable = QTalbeWidget_test()
    myTable.show()
    sys.exit(app.exec_())
