import csv
import tkinter as tk
import pandas as pd

airlines = tk. Tk()
airlines.title("administrator")
airlines.configure(background="#327fa8")
airlines.geometry("500x500")


pd.set_option('display.max_rows', None, 'display.max_columns', None)
df = pd.read_csv('airlines.csv')   # test csv file, replace with destination file
print(df)

def Delete(df, removeN):
    try:
        df = pd.read_csv('airlines.csv')
        remove = int(removeN.get())
        print(remove)
        df = df.drop(df.index[[remove]])
        df = df.reset_index(drop = True)
        print(df)
        df.to_csv('airlines.csv', index=False)
    except ValueError:
        print("That's not an index!")
    except IndexError:
        print("That index is not in the database")

removeN = tk.StringVar()

removeLabel = tk.Label(airlines, text="Enter idex of row to delete", font=('Georgia', 11, 'bold'), background='#327fa8').place(x=0, y=0)
removeEntry = tk.Entry(airlines, textvariable=removeN, width=7).place(x=220, y=3)
remove = tk.Button(airlines, text="Delete row",font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Delete(df, removeN)).place(x=290, y=0)


def Add(df, airlineNew, fcNew, bcNew):
    try:
        df = pd.read_csv('airlines.csv')
        df = df.append(pd.Series([airlineNew.get(), float(fcNew.get()), float(bcNew.get())], index=df.columns), ignore_index=True)
        print(df)
        df.to_csv('airlines.csv', index=False)
    except ValueError: # works for wrong/no entry
        print("one of the inputs was wrong")

airlineNew = tk.StringVar()
fcNew = tk.StringVar()
bcNew = tk.StringVar()

addLabel = tk.Label(airlines, text="Write Airline, First Class cost multiplier, Business Class multiplier", font=('Georgia', 10, 'bold') ,background='#327fa8').place(x=0, y=45)

countryLabel = tk.Label(airlines, text="Airline", font=('Georgia', 10, 'bold'),background='#327fa8').place(x=10, y=70)
countryEntry = tk.Entry(airlines, textvariable=airlineNew, width=15).place(x=10, y=100)

cityLabel = tk.Label(airlines, text="First Multiplier", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=120, y=70)
cityEntry = tk.Entry(airlines, textvariable=fcNew, width=20).place(x=120, y=100)

continentLabel = tk.Label(airlines, text="Business Multiplier", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=260, y=70)
continentEntry = tk.Entry(airlines, textvariable=bcNew, width=15).place(x=260, y=100)

add = tk.Button(airlines, text="Add row", font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Add(df, airlineNew, fcNew, bcNew)).place(x=370, y=96)


def Change(df, changeIndexN, changeAirlineN, changeFCN, changeBCN):
    try:
        df = pd.read_csv('airlines.csv')
        df.loc[int(changeIndexN.get())] = [changeAirlineN.get(), float(changeFCN.get()), float(changeBCN.get())]
        df = df.reset_index(drop = True)
        print(df)
        df.to_csv('airlines.csv', index = False)
    except ValueError:
        print("That's not an index!")


changeIndexN = tk.StringVar()
changeAirlineN = tk.StringVar()
changeFCN = tk.StringVar()
changeBCN = tk.StringVar()


changeLabel = tk.Label(airlines, text="Enter idex of row to edit", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=0, y=140)
changeEntry = tk.Entry(airlines, textvariable=changeIndexN, width=10).place(x=190, y=140)
replaceLabel = tk.Label(airlines, text="Write Airline, First Class multiplier, Business Class multiplier", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=0, y=165)
countryEntry = tk.Entry(airlines, textvariable=changeAirlineN, width=15).place(x=10, y=190)
countryEntry = tk.Entry(airlines, textvariable=changeFCN, width=15).place(x=120, y=190)
countryEntry = tk.Entry(airlines, textvariable=changeBCN, width=15).place(x=230, y=190)

change = tk.Button(airlines, text="Ammend row", font=('Georgia', 10, 'bold'),background='#ffa200' ,command=lambda: Change(df, changeIndexN, changeAirlineN, changeFCN, changeBCN)).place(x=120, y=230)

tk.Label(airlines, text= "file is displayed on the console" ,font=('Georgia', 10, 'bold'),background='#327fa8').place(x=250, y=300, anchor='center')

airlines.mainloop()
