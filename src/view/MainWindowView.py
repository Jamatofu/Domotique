#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import tkinter as tk

class MainWindowView:

    def __init__(self):
        self.title = "Domotique"
        self.root = tk.Tk()

    def start(self):
        self.root.mainloop()

    def loadConfiguration(self):
        self.root.title(self.title)
        self.root.attributes('-zoomed', True)
