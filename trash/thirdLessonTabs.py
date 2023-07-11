# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:37:31 2023

@author: vambolteu
"""

import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master=master
        
        self.notebook=ttk.Notebook(self.master, width=400, height=500)
        
        frame1=ttk.Frame(self.notebook)
        frame2=ttk.Frame(self.notebook)
        frame3=ttk.Frame(self.notebook)
###############################################################
        label1=ttk.Label(frame1, text="Available Energy")

        ###################################
        lab11=ttk.Label(frame1)
        lab11["text"]="Param1"
        lab11.pack(side="left")
        
        entry1=ttk.Entry(frame1)
        entry1.pack(side="left")
        
        lab12=ttk.Label(frame1)
        lab12["text"]="[J/Kg]"
        lab12.pack(side="left")
        ###############################################
        lab21=ttk.Label(frame1)
        lab21["text"]="Param2"
        lab21.pack(side="left")
        
        entry2=ttk.Entry(frame1)
        entry2.pack(side="left")
        
        lab22=ttk.Label(frame1)
        lab22["text"]="[J/Kg]"
        lab22.pack(side="left")
        ###################################
        label2=ttk.Label(frame2, text="this is Window 2")
        label3=ttk.Label(frame3, text="this is Window 3")
        
        label1.pack(padx=5, pady=5)
        label2.pack(padx=5, pady=5)
        label3.pack(padx=5, pady=5)

        frame1.pack(padx=5, pady=5)
        frame2.pack(padx=5, pady=5)
        frame3.pack(padx=5, pady=5)
        
        # label1.pack(padx=10, pady=10)
        # label2.pack(padx=10, pady=10)
        # label3.pack(padx=10, pady=10)

        # frame1.pack(padx=10, pady=10)
        # frame2.pack(padx=10, pady=10)
        # frame3.pack(padx=10, pady=10)

        self.notebook.add(frame1, text="Kinetic Energy")
        self.notebook.add(frame2, text="Thermal Energy")
        self.notebook.add(frame3, text="Electromagnetic Energy")



        self.notebook.pack(padx=5, pady=5)
        
        
        
root=tk.Tk()
root.geometry("400x500")
root.title("LoLiPoP IoT")
window=Window(root)










root.mainloop()





