import tkinter as tk
from tkinter import *
from time import strftime

#creating widgets
def CreateWidgets():
	root.dataLabel = Label(root, font=("Helvetica",50), bg="white", fg="green",
		text="DATE : "+strftime("%d/%m/%Y"))

	#Window positioning
	root.dataLabel.grid(sticky="nw")

	#creating label for display time and date
	root.timeLabel = Label(root, font=("Helvetica", 100), bg="white",fg="green")
	#Window positioning
	root.timeLabel.grid(sticky="news")

	#calling the update time
	updateTime()

def updateTime():
	root.timeLabel.config(text=strftime("%H:%M:%S"))
	root.timeLabel.after(1000, updateTime)

#Creating object root of tk
root = tk.Tk()

root.title("Digital Clock")
root.config(bg="slategray4")
root.resizable(False,False)

CreateWidgets()

root.mainloop()