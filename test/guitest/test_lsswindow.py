# *-* coding: utf8

from gui import LssWindow
import tkinter as tk


def test_lsswindow():
    root = tk.Tk()
    mainWindow = LssWindow(master=root)
    mainWindow.master.title("LightShotSniffer")
