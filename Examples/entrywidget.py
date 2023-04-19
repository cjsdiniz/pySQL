import tkinter as tk

window = tk.Tk()
entText = tk.Entry(
    master=window, bg="black", fg="white", width=40)
entText.insert(0, "What is your name?")
entText.pack()
window.mainloop()
