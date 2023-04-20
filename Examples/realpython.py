import tkinter as tk
import tkinter.ttk as ttk
window = tk.Tk()
greeting = tk.Label(text="Python rocks!")
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",
    background="black",
    width=20,
    height=10)

entry = tk.Entry(fg="yellow", bg="blue", width=50)

btn = tk.Button(
    text="Clicar",
    width=10,
    height=5,
    # bg="blue",
    # fg="yellow",
    # bg="#FFFFE0", #LightYellow
    bg="#FFD700",  # Gold
    fg="#4169E1"  # RoyalBlue
)

lbl1 = tk.Label(
    # fg="#FFD700", #Gold,
    fg="MediumSlateBlue",
    bg="Azure",
    width=20)

txt = tk.Text(
    fg="MediumSlateBlue",
    bg="Azure",
    width=20,
    height=10)

name = entry.get()
greeting.pack()
label.pack()
entry.pack()
btn.pack()
lbl1.pack()
txt.pack()
window.mainloop()
