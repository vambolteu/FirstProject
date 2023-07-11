# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 08:29:16 2023

@author: vambolteu
"""

import tkinter as tk
from tkinter import ttk


mainWindow=tk.Tk()
mainWindow.title("LoLiPoP IoT")

mainWindow.geometry("800x400")


# frame1=ttk.Frame(mainWindow)
# frame1.grid(row=0, column=5)


tabControl = ttk.Notebook(mainWindow)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl);
  
tabControl.add(tab1, text ='Kinetic Energy')
tabControl.add(tab2, text ='Thermal Energy')
tabControl.add(tab3, text= 'Electromagnetic Energy')
# tabControl.pack(expand = 1, fill ="both")
tabControl.grid(row=0, column=0)

#################################
txtParam1_1=ttk.Label(tab1)
txtParam1_1["text"]="Param1"
txtParam1_1["compound"]="bottom"

txtParam1_1.grid(row=3, column=0)

entryParam1_1=ttk.Entry(tab1)
entryParam1_1.grid(row=3, column=1)

unitParam1_1=ttk.Label(tab1, text="[Einheit]")
unitParam1_1.grid(row=3, column=2)
###################################################
###################################################
txtParam1_2=ttk.Label(tab1)
txtParam1_2["text"]="Param2"
txtParam1_2["compound"]="bottom"

txtParam1_2.grid(row=4, column=0)

entryParam1_2=ttk.Entry(tab1)
entryParam1_2.grid(row=4, column=1)

unitParam1_2=ttk.Label(tab1, text="[Einheit]")
unitParam1_2.grid(row=4, column=2)
###################################################
###################################################
txtParam1_3=ttk.Label(tab1)
txtParam1_3["text"]="Param3"
txtParam1_3["compound"]="bottom"

txtParam1_3.grid(row=5, column=0)

entryParam1_3=ttk.Entry(tab1)
entryParam1_3.grid(row=5, column=1)

unitParam1_3=ttk.Label(tab1, text="[Einheit]")
unitParam1_3.grid(row=5, column=2)
###################################################

###### Reiter 2 -------------------------------------------------------

#################################
txtParam2_1=ttk.Label(tab2)
txtParam2_1["text"]="Param1"
txtParam2_1["compound"]="bottom"

txtParam2_1.grid(row=3, column=0)

entryParam2_1=ttk.Entry(tab2)
entryParam2_1.grid(row=3, column=1)

unitParam2_1=ttk.Label(tab2, text="[Einheit]")
unitParam2_1.grid(row=3, column=2)
###################################################
###################################################
txtParam2_2=ttk.Label(tab2)
txtParam2_2["text"]="Param2"
txtParam2_2["compound"]="bottom"

txtParam2_2.grid(row=4, column=0)

entryParam2_2=ttk.Entry(tab2)
entryParam2_2.grid(row=4, column=1)

unitParam2_2=ttk.Label(tab2, text="[Einheit]")
unitParam2_2.grid(row=4, column=2)
###################################################
###################################################
txtParam2_3=ttk.Label(tab2)
txtParam2_3["text"]="Param3"
txtParam2_3["compound"]="bottom"

txtParam2_3.grid(row=5, column=0)

entryParam2_3=ttk.Entry(tab2)
entryParam2_3.grid(row=5, column=1)

unitParam2_3=ttk.Label(tab2, text="[Einheit]")
unitParam2_3.grid(row=5, column=2)



#print(lab1.keys()) gibt uns alle möglichen keys auf der Konsole aus 



# lab1=ttk.Label(window, text="Label1")
# lab1.pack()

# lab1.configure(text="Hello World")

# for item in lab1.keys():
#     print(item, ": ", lab1[item])

mainWindow.mainloop()