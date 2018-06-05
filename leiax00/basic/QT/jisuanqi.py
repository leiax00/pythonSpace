# coding: utf-8
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class JiSuanQi(QDialog):
    def __init__(self, parent=None):
        super(JiSuanQi, self).__init__(parent)
        self.browser = QTextBrowser()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setWindowTitle('my jisuanqi')


if __name__ == '__main__':
    jisuanqi = JiSuanQi()
    jisuanqi.show()
