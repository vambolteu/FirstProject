# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 08:29:16 2023

@author: vambolteu
"""

import tkinter as tk
from tkinter import ttk


mainWindow=tk.Tk()
mainWindow.title("LoLiPoP IoT")

mainWindow.geometry("600x400")


tabControl = ttk.Notebook(mainWindow)
  
tabKinEn = ttk.Frame(tabControl)
tabThermEn = ttk.Frame(tabControl)
tabElecEn = ttk.Frame(tabControl);
  
tabControl.add(tabKinEn, text ='Kinetic Energy')
tabControl.add(tabThermEn, text ='Thermal Energy')
tabControl.add(tabElecEn, text= 'Electromagnetic Energy')
# tabControl.pack(expand = 1, fill ="both")
tabControl.grid(row=0, column=0)

tabControlKin=ttk.Notebook(tabKinEn)
tabRotation=ttk.Frame(tabControlKin)
tabVibration=ttk.Frame(tabControlKin)
tabControlKin.add(tabRotation, text='Rotation')
tabControlKin.add(tabVibration, text='Vibration')

tabControlKin.grid(row=1, column=0)




###### Reiter 1, Kinetic Energy -------------------------------------------------------

#################################
txtParam1_1=ttk.Label(tabKinEn)
txtParam1_1["text"]="Param1"
txtParam1_1["compound"]="bottom"

txtParam1_1.grid(row=3, column=0, pady=20)

entryParam1_1=ttk.Entry(tabKinEn)
entryParam1_1.grid(row=3, column=1)

unitParam1_1=ttk.Label(tabKinEn, text="[Einheit]")
unitParam1_1.grid(row=3, column=2)
###################################################
###################################################
txtParam1_2=ttk.Label(tabKinEn)
txtParam1_2["text"]="Param2"
txtParam1_2["compound"]="bottom"

txtParam1_2.grid(row=4, column=0, pady=20)

entryParam1_2=ttk.Entry(tabKinEn)
entryParam1_2.grid(row=4, column=1)

unitParam1_2=ttk.Label(tabKinEn, text="[Einheit]")
unitParam1_2.grid(row=4, column=2)
###################################################
###################################################
txtParam1_3=ttk.Label(tabKinEn)
txtParam1_3["text"]="Param3"
txtParam1_3["compound"]="bottom"

txtParam1_3.grid(row=5, column=0, pady=20)

entryParam1_3=ttk.Entry(tabKinEn)
entryParam1_3.grid(row=5, column=1)

unitParam1_3=ttk.Label(tabKinEn, text="[Einheit]")
unitParam1_3.grid(row=5, column=2)
###################################################






###### Reiter 2, Thermal Energy -------------------------------------------------------

#################################
txtParam2_1=ttk.Label(tabThermEn)
txtParam2_1["text"]="Temperature Gradient \u0394T"
txtParam2_1["compound"]="bottom"

txtParam2_1.grid(row=3, column=0, pady=20)

entryParam2_1=ttk.Entry(tabThermEn)
entryParam2_1.grid(row=3, column=1)

unitParam2_1=ttk.Label(tabThermEn, text="[K]")
unitParam2_1.grid(row=3, column=2)
###################################################
###################################################
txtParam2_2=ttk.Label(tabThermEn)
txtParam2_2["text"]="Param2"
txtParam2_2["compound"]="bottom"

txtParam2_2.grid(row=4, column=0, pady=20)

entryParam2_2=ttk.Entry(tabThermEn)
entryParam2_2.grid(row=4, column=1)

unitParam2_2=ttk.Label(tabThermEn, text="[Einheit]")
unitParam2_2.grid(row=4, column=2)
###################################################
###################################################
txtParam2_3=ttk.Label(tabThermEn)
txtParam2_3["text"]="Param3"
txtParam2_3["compound"]="bottom"

txtParam2_3.grid(row=5, column=0, pady=20)

entryParam2_3=ttk.Entry(tabThermEn)
entryParam2_3.grid(row=5, column=1)

unitParam2_3=ttk.Label(tabThermEn, text="[Einheit]")
unitParam2_3.grid(row=5, column=2)






###### Reiter 3, Electromagnetic Energy -------------------------------------------------------

#################################
txtParam3_1=ttk.Label(tabElecEn)
txtParam3_1["text"]="Param1"
txtParam3_1["compound"]="bottom"

txtParam3_1.grid(row=3, column=0, pady=20)

entryParam3_1=ttk.Entry(tabElecEn)
entryParam3_1.grid(row=3, column=1)

unitParam3_1=ttk.Label(tabElecEn, text="[Einheit]")
unitParam3_1.grid(row=3, column=2)
###################################################
###################################################
txtParam3_2=ttk.Label(tabElecEn)
txtParam3_2["text"]="Param2"
txtParam3_2["compound"]="bottom"

txtParam3_2.grid(row=4, column=0, pady=20)

entryParam3_2=ttk.Entry(tabElecEn)
entryParam3_2.grid(row=4, column=1)

unitParam3_2=ttk.Label(tabElecEn, text="[Einheit]")
unitParam3_2.grid(row=4, column=2)
###################################################
###################################################
txtParam3_3=ttk.Label(tabElecEn)
txtParam3_3["text"]="Param3"
txtParam3_3["compound"]="bottom"

txtParam3_3.grid(row=5, column=0, pady=20)

entryParam3_3=ttk.Entry(tabElecEn)
entryParam3_3.grid(row=5, column=1)

unitParam3_3=ttk.Label(tabElecEn, text="[Einheit]")
unitParam3_3.grid(row=5, column=2)






# for item in lab1.keys():
#     print(item, ": ", lab1[item])

mainWindow.mainloop()