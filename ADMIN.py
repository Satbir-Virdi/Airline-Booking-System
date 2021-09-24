import tkinter as tk
from subprocess import call


def destination():
    call(["python", "ADMINdestination.py"])

def airlines():
    call(["python", "ADMINdestination.py"])

def users():
    call(["python", "ADMINusers.py"])

def deals():
    call(["python", "ADMINdeals.py"])


admin = tk. Tk()
admin.title("administrator")
admin.configure(background="#327fa8")
admin.geometry("500x500")
title = tk.Label(admin, text= "Select a file to edit", font =( 'Georgia', 10, 'bold'), background="#327fa8").place(x=250, y=10, anchor='center')
destination= tk.Button(admin, text="Destinations file", font =( 'Georgia', 10, 'bold'),background='#ffa200', command=destination).place(x=250,y=50, anchor='center')
airlines= tk.Button(admin, text="airlines file", font =( 'Georgia', 10, 'bold'),background='#ffa200', command=airlines).place(x=250,y=100, anchor='center')
Users= tk.Button(admin, text="User details file", font =( 'Georgia', 10, 'bold'),background='#ffa200',command=users).place(x=250,y=150, anchor='center')
Deals= tk.Button(admin, text="Deals file", font =( 'Georgia', 10, 'bold'),background='#ffa200', command=deals).place(x=250,y=200, anchor='center')
admin.mainloop()
