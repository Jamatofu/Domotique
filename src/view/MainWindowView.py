#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox as tkMb
class MainWindowView:

    def __init__(self):
        self.title = "Domotique"
        self.root = tk.Tk()

    def start(self):
        self.root.mainloop()

    def loadConfiguration(self):
        self.root.title(self.title)
        self.root.attributes('-zoomed', True)
        self.createMenuBar()

    def createMenuBar(self):
        menubar = tk.Menu(self.root)

        fileMenu = tk.Menu(menubar, tearoff = 0)
        fileMenu.add_command(label="Ouvrir fichier")

        aboutMenu = tk.Menu(menubar, tearoff=0)
        aboutMenu.add_command(label="Aide")
        aboutMenu.add_command(label="A propos")

        menubar.add_cascade(label="Fichier", menu=fileMenu)
        menubar.add_cascade(label="A propos", menu=aboutMenu)
        self.root.config(menu=menubar)
