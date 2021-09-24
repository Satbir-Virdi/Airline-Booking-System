import csv
import tkinter as tk
from random import randint


Checkout = tk. Tk()
Checkout.title("Checkout")
Checkout.geometry("500x500")
Checkout.configure(background = '#391c08')

listbox = tk.Listbox(Checkout, font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0', height=12, width=30)
listbox.place(x=10,y=100)

Price = tk.Listbox(Checkout, font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0', height=12, width=12)
Price.place(x=300,y=100)

x=[]

with open('temp.csv', 'r') as read: # put all contents from temp into array
    reader = csv.reader(read)
    for row in reader:
        if row:
            x.append(row)
print(x)
print(len(x))
if len(x) == 10 and float(x[0][1]): # because the password should occupy that [0][1]
    print(len(x))
    listbox.insert(tk.END, str(f'{str(x[0][0])}'))
    Price.insert(tk.END, str(f'£{round(float(x[0][1]),2)}'))
    listbox.insert(tk.END, str(f'{str(x[1][0])[-1]} Adult'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[1][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[2][0])[-1]} Child'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[2][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[3][0])}'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[3][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[4][0])}'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[4][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[5][0])[0]}eparture: {(str(x[5][0])[1:])}'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[5][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[6][0])[0]}eturn: {(str(x[6][0])[1:])}'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[6][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[7][0])[0]}eparture Date: {(str(x[7][0])[1:])}'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[7][1])) - 100}%'))
    listbox.insert(tk.END, str(f'{str(x[8][0])[0]}eturn Date: {(str(x[8][0])[1:])}'))
    Price.insert(tk.END, str(f'+ {int(100 * float(x[8][1])) - 100}%'))
    listbox.insert(tk.END, "TOTAL")
    Price.insert(tk.END, str(f'£{round(float(x[9][0]),2)}'))
else: # this is for when the user uses their MainWindow
    for i in range(1, len(x)):
        if i == len(x)-1: # put total at end
            listbox.insert(tk.END, 'TOTAL')
            Price.insert(tk.END, str(f'£{round(float(x[i][0]),2)}'))
            break
        if i > 1:
            if i == 2:
                listbox.insert(tk.END, str(f'{str(x[i][0])[-1]} Adult'))
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))
            elif i == 3:
                listbox.insert(tk.END, str(f'{str(x[i][0])[-1]} Child'))
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))
            elif i == 6:
                listbox.insert(tk.END, str(f'{(str(x[i][0])[0])}eparture: {(str(x[i][0])[1:])}'))
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))
            elif i == 7:
                listbox.insert(tk.END, str(f'{(str(x[i][0])[0])}eturn: {(str(x[i][0])[1:])}'))
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))
            elif i == 8:
                listbox.insert(tk.END, str(f'{(str(x[i][0])[0])}eparture Date: {(str(x[i][0])[1:])}'))
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))
            elif i == 9:
                listbox.insert(tk.END, str(f'{(str(x[i][0])[0])}eturn Date: {(str(x[i][0])[1:])}'))
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))

            else:
                listbox.insert(tk.END, x[i][0])
                Price.insert(tk.END, str(f'+ {int(100 * float(x[i][1])) - 100}%'))
        else:
            listbox.insert(tk.END, x[i][0])
            Price.insert(tk.END, str(f'£{x[i][1]}'))



def DealUse(*args): # add two rows for deal and new total
    listbox.configure(height=14)
    Price.configure(height=14)
    listbox.insert(tk.END, 'Deal used')
    listbox.insert(tk.END, 'New TOTAL')
    Price.insert(tk.END, str(f'{int(100 - 100*float(PotentialDeals[Deal][0]))}% off'))
    NewPrice = round((float(x[len(x)-1][0]) * float(PotentialDeals[Deal][0])), 2)
    Price.insert(tk.END, str(f'£{NewPrice}'))
    print(x[len(x)-1][0])

def complete(): # tells user theyve finished
    complete = tk.Tk()
    complete.title("finish")
    complete.geometry("200x100")
    complete.configure(background = '#391c08')
    tk.Label(complete, text="your flight is booked",font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0').pack(expand=True)
    exit

with open("deals.csv", 'r') as read:
    PotentialDeals = []
    with open('temp.csv', 'r') as TempRead:
        TempReader = csv.reader(TempRead)
        ObtainAirline = [row for idx, row in enumerate(TempReader) if idx == 8] # obtain airline and cost multiplier in 2d array
        Airline = ObtainAirline[0][0]    # obtain airline from that array
        print(ObtainAirline)
        print(Airline)
        TempRead.close()
        reader = csv.reader(read)
        for row in reader:
            if row[1] == str(' ' + Airline):
                PotentialDeals.append(row)
        print(PotentialDeals)
    if len(PotentialDeals) == 0: # deals no exist
        tk.Label(Checkout, text="Sorry, we currently have no deals for you", font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0').place(x=10,y=10)
    else:
        Deal = randint(0, len(PotentialDeals)-1)        #from array, find random deal
        print(str(f'{int(100 - 100*float(PotentialDeals[Deal][0]))}% off with {PotentialDeals[Deal][1]}'))
        tk.Label(Checkout, text="Great, we have found a deal for you", font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0').place(x=10,y=10)
        tk.Label(Checkout, text=(str(f'{int(100 - 100*float(PotentialDeals[Deal][0]))}% off with {PotentialDeals[Deal][1]}')), font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0').place(x=10,y=40)
        tk.Button(Checkout, text="Use deal", font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0', command=DealUse).place(x=10,y=70)
    TempRead.close()

tk.Button(Checkout, text='Checkout', font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#32a8a0', command=complete).place(x=10,y=390)


Checkout.mainloop()
