import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame2=ttk.Frame(root)
v = tk.StringVar()
v.set(1)

languages = [("Python", "Python"),
   	     ("Perl", "Perl"),
    	     ("Java", "Java"),
             ("C++", "C++"),
             ("C", "C")]

class Fframe:
    frame=None
    v=None

    def ShowChoice(self):
        print(self.v.get())

    def __init__(self,root,v):
        self.frame=ttk.Frame(root)
        self.frame.grid(column=0,row=0,sticky=tk.W)
        self.frame.config(width=800,height=600)
        self.frame.config(relief="sunken")
        self.v=v

        tk.Label(self.frame, 
            text="Elige el lenguaje de programacion",
            justify = tk.LEFT,
            padx = 20).pack()
        
        for language, val in languages:
            tk.Radiobutton(self.frame, 
                    text=language,
                    padx = 20, 
                    variable=self.v, 
                    command=self.ShowChoice,
                    value=val).pack(anchor=tk.W)

fppl = Fframe(root,v)

def reseteo():
    v.set(1)

btn = tk.Button(frame2,text='Resetear',command=reseteo)
btn.pack(anchor=tk.W)

frame2.grid(column=0,row=1,sticky=tk.W)
frame2.config(width=800,height=600)
frame2.config(relief="sunken")

root.mainloop()