import tkinter as tk

window = tk.Tk()

frm = tk.Frame(master=window, width=150, height=150)
frm.pack()

lbl1 = tk.Label(master=frm, text="I'm at (0,0)", bg="red")
lbl1.place(x=0, y=0)

lbl2 = tk.Label(master=frm, text="I'm at (75,75)", bg="yellow")
lbl2.place(x=75, y=75)

window.mainloop()
