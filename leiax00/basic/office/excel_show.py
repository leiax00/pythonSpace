# coding: utf-8
"""
excel演示效果，自动键入数据，并展示过程
"""
from time import sleep
from tkinter import Tk
from tkinter.messagebox import showwarning

import win32com.client as win32

notice = lambda app: showwarning(app, 'Exist?')
RANGE = range(3, 8)


def excel():
    app = 'Excel'
    xl = win32.Dispatch('{0}.Application'.format(app))
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(0.5)

    sh.Cells(1, 1).Value = 'Python-to-{0}'.format(app)
    sleep(0.5)
    for i in RANGE:
        sh.Cells(i, 1).Value = 'Line {0}'.format(i)
        sleep(0.5)
    sh.Cells(i + 2, 1).Value = 'Python-write-end:{0}'.format(app)
    notice(app)
    ss.Close(False)
    xl.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()
    excel()
