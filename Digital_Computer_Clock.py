from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Computer Clock")

fgcolor = ["aqua", "green", "salmon", "yellow", "pink", "indianred", "purple", "magenta"]


def Time(counter=0):
    if counter < 7:
        counter += 1
    else:
        counter = 0
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string, fg= fgcolor[counter])
    lbl.after(1000, Time, counter)

lbl = Label(root, font = ("arial", 160, "bold"), bg="black",fg ="aqua")

lbl.pack(anchor = "center",fill = "both",expand=1)

Time()

mainloop()
