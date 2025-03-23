import tkinter as tk
window=tk.Tk()
window.title("My First Tkinter Window")
window.geometry("500x300")
label=tk.Label(window,text="Welcome to Tkinter! Package")
label.pack()
window.mainloop()
