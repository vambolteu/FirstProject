# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:20:10 2023

@author: vambolteu_adm
"""
import tkinter as tk
from tkinter import ttk

window=tk.Tk()

window.title("LoLiPoP IoT")
# window.configure(width="", height="20")

window.geometry("800x400")

window.minsize(width=250, height=250)




label1=tk.Label(window, text="LoLiPoP IoT")

label1.pack()


# label2=tk.Label(window, text="Label2") #bg="green"/"red"/...

# label2.pack() #side="top"/"left"/...
#                 #expand=True, fill="x"/"y"/"both"
                
label2=ttk.Label(window, text="ttk Label2")
label2.pack()



window.mainloop()