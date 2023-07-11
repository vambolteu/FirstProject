# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:33:51 2023

@author: vambolteu
"""

import tkinter as tk
from tkinter import ttk
# from tkinter import *

root=tk.Tk()
root.geometry("400x500")
root.title("LoLiPoP IoT")
        # window=Window(root)
        
fr=ttk.Frame(root, width=400, height=500)
        
frame1=ttk.Frame(fr)
frame2=ttk.Frame(fr)
frame3=ttk.Frame(fr)
###############################################################
label1=ttk.Label(frame1, text="Available Energy")

###################################
lab11=ttk.Label(frame1)
lab11["text"]="Param1"
# lab11.pack(side="left")
lab11.grid(row=0,column=0)
        
        
entry1=ttk.Entry(frame1)
# entry1.pack(side="left")
lab11.grid(row=0,column=1)
lab12=ttk.Label(frame1)
lab12["text"]="[J/Kg]"
# lab12.pack(side="left")
lab11.grid(row=0,column=2)
###############################################
lab21=ttk.Label(frame1)
lab21["text"]="Param2"
# lab21.pack(side="left")
lab11.grid(row=1,column=0)
        
entry2=ttk.Entry(frame1)
# entry2.pack(side="left")
lab11.grid(row=1,column=1)
        
lab22=ttk.Label(frame1)
lab22["text"]="[J/Kg]"
# lab22.pack(side="left")
lab11.grid(row=1,column=2)
####################################

        
# button1=ttk.Button(frame1, text="but1 in frame1")
# button1.pack(side="left")
    ############################################################    
label2=ttk.Label(frame2, text="this is Window 2")
label3=ttk.Label(frame3, text="this is Window 3")
        
# label1.pack(padx=5, pady=5)
# label2.pack(padx=5, pady=5)
# label3.pack(padx=5, pady=5)

# frame1.pack(padx=5, pady=5)
# frame2.pack(padx=5, pady=5)
# frame3.pack(padx=5, pady=5)
        
#############################
label1.grid(row=0, column=0)
label2.grid(row=0, column=0)
label3.grid(row=0, column=0)

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=0)
frame3.grid(row=0, column=0)
        


# fr.pack(frame1, text="Kinetic Energy")
# fr.pack(frame2, text="Thermal Energy")
# fr.pack(frame3, text="Electromagnetic Energy")



fr.grid(row=2,column=2)



root.mainloop()