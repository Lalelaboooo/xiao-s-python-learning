#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:52:17 2018

@author: hanxiao
"""
'''
import wx

class VaR(wx.Frame):
    def __init__(self, *args, **kw):
        super(VaR,self).__init__(*args, **kw)
        
        pnl = wx.Panel(self)
        
        st = wx.StaticText(pnl, label="income_age",pos=(25,25))
        font = st.GentFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        
        self.makeMenuBar()
        
        self.CreatStatusBar()
        self.SetStatusText("Welcome to VaR!")
        
    def makeMenuBar(self):
        fileMenu = wx.Menu()
        
        VaRItem = fileMenu.Append(-1,"&hello...\tCtrl-H",
                                  "Help string shown in status bar for this \
                                  menu item")
        fileMenu.AppendSeparator()
        
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        helpMenu = wx.Menu()

app = wx.App()

frm = wx.Frame(None, title="Income age")
             
frm.Show()

app.MainLoop()
'''
import tkinter

top = 