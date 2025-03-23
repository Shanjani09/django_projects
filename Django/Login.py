import tkinter as tk
from tkinter import messagebox
def showinfo():
    if EntryBox.get()!="Shanjani" or entry.get()!="welcome":
        messagebox.showerror("Unable to login","Invalid username or password")
    else:
        messagebox.showinfo("login was Successful","Welcome!!")    
window=tk.Tk()
window.title("Login Form")
window.geometry("300x300")
username=tk.Label(window,text="Username:")
username.pack()
EntryBox=tk.Entry(window,width=20)
EntryBox.pack()
password=tk.Label(window,text="Password")
password.pack()
entry=tk.Entry(window,width=20,show="*")
entry.pack()
b1=tk.Button(window,text="Login",command=showinfo)
b1.pack()
window.mainloop()
