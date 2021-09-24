import csv
import tkinter as tk
import pandas as pd

deals = tk. Tk()
deals.title("administrator")
deals.configure(background="#327fa8")
deals.geometry("500x500")


pd.set_option('display.max_rows', None, 'display.max_columns', None)
df = pd.read_csv('deals.csv')   # test csv file, replace with destination file
print(df)

def Delete(df, removeN):
    try:
        df = pd.read_csv('deals.csv')
        x = int(removeN.get())
        print(x) # check the row entered correctly
        df = df.drop(df.index[[x]]) # remove the row
        df = df.reset_index(drop = True) # update the indexes
        print(df)
        df.to_csv('deals.csv', index=False) # update the csv file with it
    except ValueError:
        print("That's not an index!")
    except IndexError:
        print("That index is not in the database")


removeN = tk.StringVar()

removeLabel = tk.Label(deals, text="Enter idex of row to delete", font=('Georgia', 11, 'bold'), background='#327fa8').place(x=0, y=0)
removeEntry = tk.Entry(deals, textvariable=removeN, width=7).place(x=220, y=3)
remove = tk.Button(deals, text="Delete row",font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Delete(df, removeN)).place(x=290, y=0)


def Add(df, dealsN, airlineN):
    with open('airlines.csv', 'r') as read:
        reader = csv.reader(read)
        global found
        found = False
        for row in reader:
            if dealsN.get() and airlineN.get():  # check for data presence
                if str(row[0]).lower() == airlineN.get().lower(): # not case sensitive
                    try:
                        found = True
                        df = pd.read_csv('deals.csv')
                        df = df.append(pd.Series([float(dealsN.get()), (airlineN.get().lower()).capitalize()], index=df.columns), ignore_index=True)
                        print(df)
                        df.to_csv('deals.csv', index=False)
                    except ValueError:
                        print("one of the inputs was wrong")
                        break
            else:
                print("entry missing")
                break
        if found is False:
            print("airline not in database")
        return None
    reader.close()

dealsN = tk.StringVar()
airlineN = tk.StringVar()


addLabel = tk.Label(deals, text="Write Deal multiplier and Airline", font=('Georgia', 10, 'bold') ,background='#327fa8').place(x=0, y=45)

DealLabel = tk.Label(deals, text="Deal", font=('Georgia', 10, 'bold'),background='#327fa8').place(x=10, y=70)
dealsEntry = tk.Entry(deals, textvariable=dealsN, width=15).place(x=10, y=100)

AirlineLabel = tk.Label(deals, text="Airline", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=120, y=70)
airlinesEntry = tk.Entry(deals, textvariable=airlineN, width=20).place(x=120, y=100)

add = tk.Button(deals, text="Add row", font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Add(df, dealsN, airlineN)).place(x=270, y=96)




tk.Label(deals, text= "file is displayed on the console" ,font=('Georgia', 10, 'bold'),background='#327fa8').place(x=250, y=300, anchor='center')





deals.mainloop()
