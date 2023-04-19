# Geometry Nanagers
# .pack()
# .place()
# .grid()

# PACK
import tkinter as tk

window = tk.Tk()

# frm1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frm1.pack(fill=tk.Y, side=tk.LEFT)

# frm2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frm2.pack(fill=tk.X, side=tk.BOTTOM)

# frm3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frm3.pack(fill=tk.Y, side=tk.RIGHT)

# frm4 = tk.Frame(master=window, width=25, height=25, bg="green")
# frm4.pack(fill=tk.X, side=tk.TOP)

frm1 = tk.Frame(master=window, width=100, height=100, bg="red")
frm1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frm2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frm2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frm3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frm3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frm4 = tk.Frame(master=window, width=25, height=25, bg="green")
frm4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
