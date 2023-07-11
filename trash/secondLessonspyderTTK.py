# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:56:46 2023

@author: vambolteu
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window=tk.Tk()

window.geometry("800x400")


im=Image.open("powerlogo.png").resize((100,100))
photo=ImageTk.PhotoImage(im)


# lab1=ttk.Label(window, text="dies ist ein Logo", image=photo, compound="top")
lab1=ttk.Label(window)
lab1["text"]="neuer Text"
lab1["image"]=photo
lab1["compound"]="bottom"

lab1.pack()

#print(lab1.keys()) gibt uns alle möglichen keys auf der Konsole aus 



# lab1=ttk.Label(window, text="Label1")
# lab1.pack()

# lab1.configure(text="Hello World")

for item in lab1.keys():
    print(item, ": ", lab1[item])

window.mainloop()



