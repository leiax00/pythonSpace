# -*- coding: utf-8 -*-
import wx


class MyFrame1(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"My Tools", pos=wx.DefaultPosition,
                          size=wx.Size(1366, 768), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        fgSizer1 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gSizer2 = wx.GridSizer(1, 9, 0, 0)

        gSizer2.SetMinSize(wx.Size(100, 30))
        self.主页 = wx.Button(self, wx.ID_ANY, u"主页", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer2.Add(self.主页, 0, wx.ALL, 5)

        self.DB配置 = wx.Button(self, wx.ID_ANY, u"DB配置", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer2.Add(self.DB配置, 0, wx.ALL, 5)

        self.XML配置 = wx.Button(self, wx.ID_ANY, u"XML配置", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer2.Add(self.XML配置, 0, wx.ALL, 5)

        self.Properties配置 = wx.Button(self, wx.ID_ANY, u"Properties配置", wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizer2.Add(self.Properties配置, 0, wx.ALL, 5)

        fgSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(2, 2, 0, 0)

        gSizer3.SetMinSize(wx.Size(1366, 400))
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_treeCtrl4 = wx.TreeCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 400),
                                       wx.TR_DEFAULT_STYLE)
        bSizer3.Add(self.m_treeCtrl4, 0, wx.ALL, 5)

        self.m_checkList1 = wx.CheckListBox(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, None, 0)
        bSizer3.Add(self.m_checkList1, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        gSizer3.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add(gSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.DB配置.Bind(wx.EVT_LEFT_DCLICK, self.open_db_content())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def open_db_conten(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    myFrame = MyFrame1()
    myFrame.Show()
    app.MainLoop()
