import tkinter as tk
from time import strftime

def time():
    string = strftime("%I:%M:%S %p \n %D")
    label.config(text = string)
    label.after(1000,time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root,font=("Digital-7 Mono",60,),bg = "black", fg= "yellow")
label.pack(anchor= "center")

time()

root.mainloop()
