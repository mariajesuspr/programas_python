from tkinter import *

def blink():
    e.config(bg='green')
    e.after(1500, lambda: e.config(bg='white')) # after 1000ms

root = Tk()
root.geometry("400x400")
e = Entry(root)
e.pack()
b = Button(root, text='blink', command=blink)
b.pack()
root.mainloop()