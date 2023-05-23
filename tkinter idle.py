from tkinter import *

root = Tk()

root.geometry("500x500")
root.title("My first GUI")

label = Tk.Label(root, text="Hello!!", font=('Arial', 18))
label.pack()

root.mainloop()
