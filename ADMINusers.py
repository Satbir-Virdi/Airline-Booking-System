import csv
import tkinter as tk
import pandas as pd

users = tk. Tk()
users.title("administrator")
users.configure(background="#327fa8")
users.geometry("500x500")


pd.set_option('display.max_rows', None, 'display.max_columns', None)
df = pd.read_csv('RegisterLogin.csv')   # test csv file, replace with destination file
print(df)

def Delete(df, removeN):
    try:
        df = pd.read_csv('RegisterLogin.csv')
        x = int(removeN.get())
        print(x)
        df = df.drop(df.index[[x]])
        df = df.reset_index(drop = True)
        print(df)
        df.to_csv('RegisterLogin.csv', index=False)
    except ValueError:
        print("That's not an index!")
    except IndexError:
        print("That index is not in the database")

removeN = tk.StringVar()

removeLabel = tk.Label(users, text="Enter idex of row to delete", font=('Georgia', 11, 'bold'), background='#327fa8').place(x=0, y=0)
removeEntry = tk.Entry(users, textvariable=removeN, width=7).place(x=220, y=3)
remove = tk.Button(users, text="Delete row",font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Delete(df, removeN)).place(x=290, y=0)


def Add(df, UsernameN, PasswordN, EmailN):
    try:
        df = pd.read_csv('RegisterLogin.csv')
        df = df.append(pd.Series([UsernameN.get(), PasswordN.get(), EmailN.get()], index=df.columns), ignore_index=True)
        print(df)
        df.to_csv('RegisterLogin.csv', index=False)
    except ValueError:  # works for any error
        print("one of the inputs was wrong")


UsernameN = tk.StringVar()
PasswordN = tk.StringVar()
EmailN = tk.StringVar()

addLabel = tk.Label(users, text="Write Username, Password, Email", font=('Georgia', 10, 'bold') ,background='#327fa8').place(x=0, y=45)

countryLabel = tk.Label(users, text="Username", font=('Georgia', 10, 'bold'),background='#327fa8').place(x=10, y=70)
countryEntry = tk.Entry(users, textvariable=UsernameN, width=15).place(x=10, y=100)

cityLabel = tk.Label(users, text="Password", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=120, y=70)
cityEntry = tk.Entry(users, textvariable=PasswordN, width=20).place(x=120, y=100)

continentLabel = tk.Label(users, text="Email", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=260, y=70)
continentEntry = tk.Entry(users, textvariable=EmailN, width=15).place(x=260, y=100)

add = tk.Button(users, text="Add row", font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Add(df, UsernameN, PasswordN, EmailN)).place(x=370, y=96)


def Change(df, changeIndexN, changeUsernameN, changePasswordN, changeEmailN):
    try:
        df = pd.read_csv('RegisterLogin.csv')
        df.loc[int(changeIndexN.get())] = [changeUsernameN.get(), changePasswordN.get(), changeEmailN.get()]
        df = df.reset_index(drop = True)
        print(df)
        df.to_csv('RegisterLogin.csv', index = False)
    except ValueError:
        print("That's not an index!")


changeIndexN = tk.StringVar()
changeUsernameN = tk.StringVar()
changePasswordN = tk.StringVar()
changeEmailN = tk.StringVar()


changeLabel = tk.Label(users, text="Enter idex of row to edit", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=0, y=140)
changeEntry = tk.Entry(users, textvariable=changeIndexN, width=10).place(x=190, y=140)
replaceLabel = tk.Label(users, text="Write Username, Password, Email", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=0, y=165)
countryEntry = tk.Entry(users, textvariable=changeUsernameN, width=15).place(x=10, y=190)
countryEntry = tk.Entry(users, textvariable=changePasswordN, width=15).place(x=120, y=190)
countryEntry = tk.Entry(users, textvariable=changeEmailN, width=15).place(x=230, y=190)

change = tk.Button(users, text="Ammend row", font=('Georgia', 10, 'bold'),background='#ffa200' ,command=lambda: Change(df, changeIndexN, changeUsernameN, changePasswordN, changeEmailN)).place(x=120, y=230)

tk.Label(users, text= "file is displayed on the console" ,font=('Georgia', 10, 'bold'),background='#327fa8').place(x=250, y=300, anchor='center')

users.mainloop()
