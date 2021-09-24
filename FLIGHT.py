import csv
import tkinter as tk
from subprocess import call
global output


def bong(*args):
    pass


FLIGHT = tk. Tk()
FLIGHT.title("Flight")
FLIGHT.geometry("800x800")
FLIGHT.configure(background = '#391c08')

temp = open('temp.csv', 'r')




       #this stores the chosen value in the optionmenu for OptionNam
def Continent():
    def countryFilter(*args):
        x = continent.get()
        OptionName = []

        def shorter(*args):
            y = country.get()
            OptionName = []
            destination = tk.StringVar(FLIGHT)
            with open("destination.csv", 'r') as read:      # This gets the cost of the chosen city/destination
                reader = csv.reader(read)
                for row in reader:
                    if y == row[0]:
                        OptionName.append(str(f'{(row[1])}'))
                        RunningCost = float(row[3])     # update running cost

                        tk.Label(FLIGHT, text=str(f'£{float(row[3])}'),font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15).place(x=290,y=130)
            option = tk.OptionMenu(FLIGHT, destination, *OptionName)
            option.config(font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15)
            option.place(x=120, y=130)
            destination.set(OptionName[0])
            read.close()
            def showDestination(*args):

                with open("temp.csv", 'r+') as appendTemp:
                      #I tried w+ and r+ but there were logical errors which i could not solve
                    listK = [destination.get(), RunningCost]
                    readerS = csv.reader(appendTemp)
                    csvInput = list(readerS)    # put Temp contents in list
                    csvInput = [x for x in csvInput if x]  # remove empty lists from the list
                    csvInput.append([])  # create a space for the new data to be added
                    csvInput[0] = (listK)
                    csvInput.append([])  # update running cost in Temp
                    print(csvInput)  # See Temp array
                    AdultN()
                appendTemp.close()
                with open("temp.csv", 'w') as appendTemp:
                    writer = csv.writer(appendTemp)
                    appendTemp.truncate()  # clear temp
                    writer.writerows(csvInput)  # input csvInput into Temp
                    appendTemp.close()
                    CostCheck()
                return None

            showDestination()
            destination.trace('w', showDestination)       # it works sort of, when another city of the same country is chosen, the city is printed but not the country
            print(country.get())                   # make it write the city chosen to temp.csv. Go backward through list of countries/cities till 1st chosen
        with open("destination.csv", "r") as read:  # make a running cost total etc
            reader = csv.reader(read)
            for row in reader:
                if row[2] == x:
                    OptionName.append(str(row[0]))
            OptionName = list(dict.fromkeys(OptionName))            # remove duplicates
        country = tk.StringVar(FLIGHT)
        country.set(OptionName[0])
        CountryS = tk.OptionMenu(FLIGHT, country, *OptionName)    # create optionmenu for country with selected continent
        CountryS.config(font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15)
        CountryS.place(x=150, y=96)
        country.trace('w', shorter)

    OptionName = []
    with open("destination.csv", 'r') as read:
        reader = csv.reader(read)
        for row in reader:
            if row[2]:  # check the cell is not empty
                OptionName.append(row[2])
        OptionName = list(dict.fromkeys(OptionName))    # remove duplicates
        OptionName.remove(OptionName[0])    #remove column title from array

    continent = tk.StringVar(FLIGHT)
    continent.set(OptionName[0])
    continent.trace('w', countryFilter)
    ContinentS = tk.OptionMenu(FLIGHT, continent, *OptionName)
    ContinentS.config(font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15)
    ContinentS.place(x=150, y=66)
    print(continent)
Continent()



tk.Label(FLIGHT, text='Select Continent: ', font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x=10, y=70)
tk.Label(FLIGHT, text='Select Country: ', font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x=10, y=100)
c = tk.Label(FLIGHT, text=' Destination: ', font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x= 8, y = 130)

def AdultN():

    def ShowAdultN(*args):
        with open("temp.csv", 'r+') as appendTemp:
            if AdultNchoose.get() == '1':     # multiplier foramount of adults
                x = 1.1
            elif AdultNchoose.get() == '2':
                x = 1.2
            else:
                x = 1.3
            listK = ['Adult' + AdultNchoose.get(), x]
            readerS = csv.reader(appendTemp)
            csvInput = list(readerS) # Temp file rows as items in list
            csvInput = [x for x in csvInput if x]
            csvInput.append([]) #add empty list for listk
            csvInput[1] = (listK)
            print(csvInput)
            ChildN()
        appendTemp.close()
        with open("temp.csv", 'w') as appendTemp:
            writer = csv.writer(appendTemp)
            appendTemp.truncate()
            writer.writerows(csvInput) # update Temp with new contents
            appendTemp.close()
            CostCheck()
        return None
    AdultNumber = [1, 2, 3]
    AdultNchoose = tk.StringVar()
    AdultNchoose.set(AdultNumber[0])
    AdultNchoose.trace("w", ShowAdultN)
    AdultN = tk.OptionMenu(FLIGHT, AdultNchoose, *AdultNumber)
    AdultN.config( font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08')
    AdultN.place(x=220, y=205, anchor='center')

    def ChildN():

        def ShowChildN(*args):
            with open("temp.csv", 'r+') as appendTemp:
                if ChildNchoose.get() == '0':
                    x = 1
                elif ChildNchoose.get() =='1':
                    x = 1.1
                elif ChildNchoose.get() =='2':
                    x = 1.2
                elif ChildNchoose.get() =='3':
                    x = 1.3
                elif ChildNchoose.get() =='4':
                    x = 1.4
                listK = ['Child' + ChildNchoose.get(), x]
                readerS = csv.reader(appendTemp)
                csvInput = list(readerS) # Temp file rows as items in list
                csvInput = [x for x in csvInput if x]
                csvInput.append([]) #add empty list for listk
                csvInput[2] = (listK)
                print(csvInput)
                Airline()
            appendTemp.close()
            with open("temp.csv", 'w') as appendTemp:
                writer = csv.writer(appendTemp)
                appendTemp.truncate()
                writer.writerows(csvInput)
                appendTemp.close()
                CostCheck()
            return None
        ChildNumber = [0, 1, 2, 3, 4]
        ChildNchoose = tk.StringVar()
        ChildNchoose.set(ChildNumber[0])
        ChildNchoose.trace("w", ShowChildN)
        ChildN = tk.OptionMenu(FLIGHT, ChildNchoose, *ChildNumber)
        ChildN.config( font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08')
        ChildN.place(x=220, y=235, anchor='center')



tk.Label(FLIGHT, text=' Choose Adult Number: ', font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x= 10, y = 190)
tk.Label(FLIGHT, text=' Choose Child Number: ', font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x= 10, y = 220)


def Airline():
    OptionName = []
    with open('airlines.csv', 'r') as read:
        reader = csv.reader(read)
        for row in reader:
            if row[0] != 'airline': # no add the column header 'airline' from the option menu
                OptionName.append(row[0])
    airlineChoose = tk.StringVar()
    airlineChoose.set(OptionName[0])
    airlinechosen = airlineChoose.get()
    def showAirline(*args):
        with open("temp.csv", 'r+') as appendTemp:
            listK = [airlineChoose.get(), 1]
            readerS = csv.reader(appendTemp)
            csvInput = list(readerS) # Temp file rows as items in list
            csvInput = [x for x in csvInput if x]
            csvInput.append([]) #add empty list for listk
            csvInput[3] = (listK)

            print(csvInput)
            seat(airlinechosen)
        appendTemp.close()
        with open("temp.csv", 'w') as appendTemp:
            writer = csv.writer(appendTemp)
            appendTemp.truncate()
            writer.writerows(csvInput)
            appendTemp.close()
            CostCheck()

    airlineChoose.trace("w", showAirline)
    SeatN = tk.OptionMenu(FLIGHT, airlineChoose, *OptionName)
    SeatN.config( font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15)
    SeatN.place(x=140, y=265)

tk.Label(FLIGHT, text=' Choose Airline: ', font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x= 10, y = 270)


def seat(airlinechosen):
    def showClass(*args):
        with open("temp.csv", 'r+') as appendTemp:
            with open('airlines.csv', 'r') as read:
                reader = csv.reader(read)
                for row in reader:
                    if row[0] == airlinechosen:
                        if SeatNtype.get() == 'Economy':
                            x = 1
                        elif SeatNtype.get() == 'Business':
                            x = float(row[2])
                        else:
                            x = float(row[1])
            listK = [SeatNtype.get(), x]
            readerS = csv.reader(appendTemp)
            csvInput = list(readerS)
            csvInput = [x for x in csvInput if x]
            csvInput.append([])
            csvInput[4] = (listK)
            print(csvInput)
            Airport()
        appendTemp.close()
        with open("temp.csv", 'w') as appendTemp:
            writer = csv.writer(appendTemp)
            appendTemp.truncate()
            writer.writerows(csvInput)
            appendTemp.close()
            CostCheck()
    SeatType = ["Economy", "Business", "First Class"]
    SeatNtype = tk.StringVar()
    SeatNtype.set(SeatType[0])
    SeatNtype.trace("w", showClass)
    SeatN = tk.OptionMenu(FLIGHT, SeatNtype, *SeatType)
    SeatN.config( font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15)
    SeatN.place(x=220, y=315, anchor='center')



tk.Label(FLIGHT, text="Select Class: ",font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08').place(x=13, y=300)


def Airport():
    def ShowAirportDep(*args):
        with open("temp.csv", 'r+') as appendTemp:
            listK = ['D ' + airportDep.get(), 1] # d for Departure, can distinguish
            readerS = csv.reader(appendTemp)
            csvInput = list(readerS)
            csvInput = [x for x in csvInput if x]
            csvInput.append([])
            csvInput[5] = (listK)
            print(csvInput)
            AirportRet()
        appendTemp.close()
        with open("temp.csv", 'w') as appendTemp:
            writer = csv.writer(appendTemp)
            appendTemp.truncate()
            writer.writerows(csvInput)
            appendTemp.close()
            CostCheck()

    AirportDep = ["London - Heathrow", "London - Stansted", "London - Luton", "London - Gatwick","Manchester", "Birmingham", "Belfast International", "Edinburgh"]
    airportDep = tk.StringVar()
    airportDep.set(AirportDep[0])
    airportDep.trace("w", ShowAirportDep)
    AirportS = tk.OptionMenu(FLIGHT, airportDep, *AirportDep)
    AirportS.config(font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08',width=15)
    AirportS.place(x=200, y =350)

    def AirportRet():
        def ShowAirportRet(*args):
            with open("temp.csv", 'r+') as appendTemp:
                listK = ['R ' + airportRet.get(), 1] # R for Departure, can distinguish
                readerS = csv.reader(appendTemp)
                csvInput = list(readerS)
                csvInput = [x for x in csvInput if x]
                csvInput.append([])
                csvInput[6] = (listK)
                print(csvInput)
                Date()
            appendTemp.close()
            with open("temp.csv", 'w') as appendTemp:
                writer = csv.writer(appendTemp)
                appendTemp.truncate()
                writer.writerows(csvInput)
                appendTemp.close()
                CostCheck()
        AirportRet = ["London - Heathrow", "London - Stansted", "London - Luton", "London - Gatwick","Manchester", "Birmingham", "Belfast International", "Edinburgh"]
        airportRet = tk.StringVar()
        airportRet.set(AirportRet[0])
        airportRet.trace("w", ShowAirportRet)
        AirportRetS = tk.OptionMenu(FLIGHT, airportRet, *AirportRet)
        AirportRetS.config(text="Select Airport : ", font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',highlightbackground='#391c08')
        AirportRetS.place(x=180, y = 380)

tk.Label(FLIGHT, text="Select Departure Airport : ", font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F').place(x=10, y=350)
tk.Label(FLIGHT, text='Select Return Airport: ', font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#00DA5F').place(x=10, y=380)


def Date():
    def WrongDate():
        def e2():
            WrongDate.destroy()
        WrongDate = tk.Tk()
        WrongDate.title("Wrong Destination")
        WrongDate.geometry("200x70")
        WrongDate.configure(background="#391c08")
        tk.Label(WrongDate, text="Date was incorrect", font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F',  width=20).pack()
        tk.Button(WrongDate, text="okay", font=('Georgia', 10, 'bold'), background='#391c08', foreground='#00DA5F', width=20, command=e2).pack()

    Dday = tk.StringVar()
    Dmonth = tk.StringVar()
    Dyear = tk.StringVar()
    tk.Entry(FLIGHT, textvariable=Dday, font = ('Georgia', 10, 'bold'), background = '#00DA5F', width=4).place(x=180, y=430)
    tk.Entry(FLIGHT, textvariable=Dmonth, font = ('Georgia', 10, 'bold'), background = '#00DA5F', width=4).place(x=230, y=430)
    tk.Entry(FLIGHT, textvariable=Dyear, font = ('Georgia', 10, 'bold'), background = '#00DA5F', width=4).place(x=280, y=430)

    def ReturnDate():
        Rday = tk.StringVar()
        Rmonth = tk.StringVar()
        Ryear = tk.StringVar()      # variables and entry boxes to entry date as DD/MM/YYYY
        tk.Entry(FLIGHT, textvariable=Rday, font = ('Georgia', 10, 'bold'), background = '#00DA5F', width=4).place(x=180, y=460)
        tk.Entry(FLIGHT, textvariable=Rmonth, font = ('Georgia', 10, 'bold'), background = '#00DA5F', width=4).place(x=230, y=460)
        tk.Entry(FLIGHT, textvariable=Ryear, font = ('Georgia', 10, 'bold'), background = '#00DA5F', width=4).place(x=280, y=460)
        def checkR(Rday, Rmonth, Ryear):
            try:
                d = int(Rday.get())
                m = int(Rmonth.get())       # checks the month and day exist in that month, then write it as a list
                y = int(Ryear.get())
                if m > 0 and m < 13:
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12: # check months with 31 days
                        if d > 0 and d < 32:
                            Rdate = str(f'{Rday.get()}/{Rmonth.get()}/{Ryear.get()}')
                        else:
                            WrongDate()
                    elif m == 4 or m == 6 or m == 9 or m == 11: # check months with 30 days
                        if d > 0 and d < 31:
                            Rdate = str(f'{Rday.get()}/{Rmonth.get()}/{Ryear.get()}')
                        else:
                            WrongDate()
                    elif m == 2: # check february
                        if d > 0 and d < 29:
                            Rdate = str(f'{Rday.get()}/{Rmonth.get()}/{Ryear.get()}')
                        else:
                            WrongDate()
                    else:
                        WrongDate()
                with open("temp.csv", 'r+') as appendTemp:
                #I tried w+ and r+ but there were logical errors which i could not solve
                    listK = ['R ' + Rdate, 1] # R for Return, can distinguish
                    readerS = csv.reader(appendTemp)
                    csvInput = list(readerS)
                    csvInput = [x for x in csvInput if x]
                    csvInput.append([])
                    csvInput[8] = (listK)
                    print(csvInput)
                    def Checkout():
                        with open('temp.csv', 'a') as append:
                            writer = csv.writer(append)
                            writer.writerow([CostCheck(), 1])
                        call(["Python", "CHECKOUT.py"])

                appendTemp.close()
                with open("temp.csv", 'w') as appendTemp:
                    writer = csv.writer(appendTemp)
                    appendTemp.truncate()
                    writer.writerows(csvInput)
                    appendTemp.close()
                    CostCheck()
                    Checkout()

            except TypeError:
                WrongDate()
            except ValueError:
                WrongDate()

        tk.Button(FLIGHT, text='Checkout', font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#00DA5F', command=lambda: checkR(Rday, Rmonth, Ryear)).place(x=330, y=460)


    def check(Dday, Dmonth, Dyear):
        try:
            d = int(Dday.get())
            m = int(Dmonth.get())
            y = int(Dyear.get())
            if m > 0 and m < 13:
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    if d > 0 and d < 32:
                        Ddate = str(f'{Dday.get()}/{Dmonth.get()}/{Dyear.get()}')
                    else:
                        WrongDate()
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if d > 0 and d < 31:
                        Ddate = str(f'{Dday.get()}/{Dmonth.get()}/{Dyear.get()}')
                    else:
                        WrongDate()
                elif m == 2:
                    if d > 0 and d < 29:
                        Ddate = str(f'{Dday.get()}/{Dmonth.get()}/{Dyear.get()}')
                    else:
                        WrongDate()
                else:
                    WrongDate()
            with open("temp.csv", 'r+') as appendTemp:
                listK = ['D ' + Ddate, 1] # d for Departure, can distinguish
                readerS = csv.reader(appendTemp)
                csvInput = list(readerS)
                csvInput = [x for x in csvInput if x]
                csvInput.append([])
                csvInput[7] = (listK)
                print(csvInput)
                ReturnDate()
            appendTemp.close()
            with open("temp.csv", 'w') as appendTemp:
                writer = csv.writer(appendTemp)
                appendTemp.truncate()
                writer.writerows(csvInput)
                appendTemp.close()
                CostCheck()
        except TypeError:
            WrongDate()
        except ValueError:
            WrongDate()

    tk.Button(FLIGHT, text='Open Departure date Entry boxes', font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#00DA5F', command=lambda: check(Dday, Dmonth,Dyear)).place(x=330, y=430)

tk.Label(FLIGHT, text='Write Departure Date: ', font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#00DA5F').place(x=10, y=430)
tk.Label(FLIGHT, text='Select Return date: ', font = ('Georgia', 10, 'bold'), background = '#391c08', foreground = '#00DA5F').place(x=10, y=460)

def CostCheck():
    with open('temp.csv', 'r') as read:
        reader = csv.reader(read)
        csvInput = list(reader)
        csvInput = [x for x in csvInput if x]
        CurrentCost = 1
        for row in csvInput:
            print(row[1])
            try:
                CurrentCost = CurrentCost * float(row[1])
                tk.Label(FLIGHT, text=str('£' + str(int(CurrentCost))), font=('Georgia', 15, 'bold'), background='#391c08', foreground='#328ba8',highlightbackground='#391c08').place(x=400,y=400)
            except ValueError:
                pass

    return CurrentCost
FLIGHT.mainloop()
