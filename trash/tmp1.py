# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 08:24:53 2023

@author: vambolteu
"""

from tkinter import *


root = Tk()
root.resizable(width=False, height=False)

w = Canvas(root, width=500, height=500)
w.pack()


textInput = Entry(w, width=50, borderwidth=2)  # w, instead of root
textInput.pack()


def myClick():
    myLabel = Label(root, text=textInput.get())
    myLabel.pack()


def shutDown():
    exitProgram = exit()
    exitProgram.pack()


myButton = Button(w, text="Start", command=myClick)  # w, instead of root
myButton.pack(side=LEFT, padx=20, pady=25)
myButton2 = Button(w, text="Stop", command=shutDown)  # w, instead of root
myButton2.pack(side=RIGHT, padx=20, pady=25)


root.mainloop()