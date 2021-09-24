import csv
import tkinter as tk
import pandas as pd


destination = tk. Tk()
destination.title("administrator")
destination.configure(background="#327fa8")
destination.geometry("500x500")


pd.set_option('display.max_rows', None, 'display.max_columns', None) # shows dataframe of any size
df = pd.read_csv('destination.csv')
print(df)  # show user the file


def Delete(df, removeN):
    try:
        df = pd.read_csv('destination.csv')  # read csv file and store in variable/ dataframe
        x = int(removeN.get())  # the row the user wants to remove
        df = df.drop(df.index[[x]])  # removes the row from the dataframe
        df = df.reset_index(drop = True)  # index no match csv. So indexes are reset after the removal
        print(df) # print the updated file
        df.to_csv('destination.csv', index=False) # update the csv file with the dataframe
    except ValueError:
        print("That's not an index!") # A notification in console for an error
    except IndexError:
        print("That index is not in the database")


def Add(df, countryNew, cityNew, continentNew, priceNew):
    try:
        if countryNew.get() and cityNew.get() and continentNew.get() and (int(priceNew.get()) or float(priceNew.get())):
            df = pd.read_csv('destination.csv')
            df = df.append(pd.Series([' ' + countryNew.get(), ' ' + cityNew.get(), ' ' + continentNew.get(), ' ' + str(priceNew.get())], index=df.columns), ignore_index=True)
            print(df)
            df.to_csv('destination.csv', index=False)
        else:
            print("an entry is missing")
    except ValueError:
        print("that is not a price")




def Change(df, changeIndexN, countryChangeN, cityChangeN, continentChangeN, priceChangeN):
        try:
            if int(changeIndexN.get()) and countryChangeN.get() and cityChangeN.get() and continentChangeN.get() and priceChangeN.get():
                df = pd.read_csv('destination.csv') # this changes the appropriate row with the new data
                if len(df.index) > int(changeIndexN.get()) and int(changeIndexN.get()) > 0:
                    df.loc[int(changeIndexN.get())] = [countryChangeN.get(),' ' + cityChangeN.get(), ' ' + continentChangeN.get(),' ' + int(priceChangeN.get())]
                    df = df.reset_index(drop = True)
                    print(df)
                    df.to_csv('destination.csv', index = False)
                else:
                    print("wrong index")
            else:
                print("entry missing")
        except ValueError:
            print("There was an error in the data entered")
        except TypeError:
            df = pd.read_csv('destination.csv')
            df.loc[int(changeIndexN.get())] = [countryChangeN.get(),' ' + cityChangeN.get(), ' ' + continentChangeN.get(),' ' + priceChangeN.get()]
            df = df.reset_index(drop = True)
            print(df)




priceChangeN = tk.StringVar()
priceNew = tk.StringVar()
removeN = tk.StringVar()
countryNew = tk.StringVar()
cityNew = tk.StringVar()
continentNew = tk.StringVar()
changeIndexN = tk.StringVar()
countryChangeN = tk.StringVar()
cityChangeN = tk.StringVar()
continentChangeN = tk.StringVar()

removeLabel = tk.Label(destination, text="Enter idex of row to delete", font=('Georgia', 11, 'bold'), background='#327fa8').place(x=0, y=0)
removeEntry = tk.Entry(destination, textvariable=removeN, width=7).place(x=220, y=3)
remove = tk.Button(destination, text="Delete row",font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Delete(df, removeN)).place(x=290, y=0)


addLabel = tk.Label(destination, text="Write Country, City, Continent, Price to Add", font=('Georgia', 10, 'bold') ,background='#327fa8').place(x=0, y=45)

countryLabel = tk.Label(destination, text="Country", font=('Georgia', 10, 'bold'),background='#327fa8').place(x=10, y=70)
countryEntry = tk.Entry(destination, textvariable=countryNew, width=15).place(x=10, y=100)

cityLabel = tk.Label(destination, text="City", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=120, y=70)
cityEntry = tk.Entry(destination, textvariable=cityNew, width=15).place(x=120, y=100)

continentLabel = tk.Label(destination, text="Continent", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=230, y=70)
continentEntry = tk.Entry(destination, textvariable=continentNew, width=15).place(x=230, y=100)

continentLabel = tk.Label(destination, text="Price", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=340, y=70)
continentEntry = tk.Entry(destination, textvariable=priceNew, width=15).place(x=340, y=100)

add = tk.Button(destination, text="Add row", font=('Georgia', 10, 'bold'),background='#ffa200', command=lambda: Add(df, countryNew, cityNew, continentNew, priceNew)).place(x=340, y=45)

changeLabel = tk.Label(destination, text="Enter idex of row to edit", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=0, y=140)
changeEntry = tk.Entry(destination, textvariable=changeIndexN, width=10).place(x=190, y=140)
replaceLabel = tk.Label(destination, text="Write Country, City, Continent, Price", font=('Georgia', 10, 'bold'), background='#327fa8').place(x=72, y=165)
countryEntry = tk.Entry(destination, textvariable=countryChangeN, width=15).place(x=10, y=190)
cityEntry = tk.Entry(destination, textvariable=cityChangeN, width=15).place(x=120, y=190)
continentEntry = tk.Entry(destination, textvariable=continentChangeN, width=15).place(x=230, y=190)
priceEntry = tk.Entry(destination, textvariable=priceChangeN, width=15).place(x=340, y=190)

change = tk.Button(destination, text="Ammend row", font=('Georgia', 10, 'bold'),background='#ffa200' ,command=lambda: Change(df, changeIndexN, countryChangeN, cityChangeN, continentChangeN, priceChangeN)).place(x=120, y=230)

tk.Label(destination, text= "file is displayed on the console" ,font=('Georgia', 10, 'bold'),background='#327fa8').place(x=250, y=300, anchor='center')

destination.mainloop()
