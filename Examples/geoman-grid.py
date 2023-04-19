'''
Geometry manager: Grid
'''

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frm = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        frm.grid(row=i, column=j)
        lbl = tk.Label(master=frm, text=f"Row {i}\nColumn {j}")
        lbl.pack()

window.mainloop()
