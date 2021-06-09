from tkinter import *
import tkinter
import datetime
import pickle
from pickle import *


root = Tk()
root.title('Hotel Havana Accounting Softare')
root.geometry('1500x900')

Topic = Label(root, text='Select an Option to get Started')
Topic.pack(padx=12, pady=12)

def reserve():
    newWindow = tkinter.Toplevel(root)
    newWindow.title('Reservation Handler')
    newWindow.geometry('1110x600')

    info = Label(newWindow, text='Enter Guests Details: ', font=('Arial', 35))
    info.pack()

    newFrame = Frame(newWindow)

    
    entry1 = Entry(newFrame, textvariable=StringVar, width='30', bg='lightyellow', cursor='dot')
    nom = Label(newFrame, text='Full Name', font=('Arial', 20))
    nom.pack()
    entry1.pack()

    entry2 = Entry(newFrame, textvariable=StringVar, width='30', bg='lightyellow', cursor='dot')
    arrival = Label(newFrame, text='  Arrival Date', font=('Arial', 20))
    arrival.pack()
    entry2.pack()
    
    entry5 = Entry(newFrame, textvariable=StringVar, width='30', bg='lightyellow', cursor='dot')
    depart = Label(newFrame, text='  Departure Date', font=('Arial', 20))
    depart.pack()
    entry5.pack()

    entry3 = Entry(newFrame, textvariable=StringVar, width='30', bg='lightyellow', cursor='dot')
    numero = Label(newFrame, text='  Phone Number', font=('Arial', 20))
    numero.pack()
    entry3.pack()

    entry6 = Entry(newFrame, textvariable=StringVar, width='30', bg='lightyellow', cursor='dot')
    room = Label(newFrame, text='  Room Number/Price', font=('Arial', 20))
    room.pack()
    entry6.pack()

    entry7 = Entry(newFrame, textvariable=StringVar, width='30', bg='lightyellow', cursor='dot')
    staff = Label(newFrame, text='  Staff Name', font=('Arial', 20))
    staff.pack()
    entry7.pack()

    res_dt = datetime.datetime.now()
    res_d = [res_dt.day, res_dt.month, res_dt.year]
    res_t = [res_dt.hour, res_dt.minute, res_dt.second]

    def storage(dict): 
        picdic = {}
        dbfile = open('C://Users/USER/Desktop/freelance/py/tkinter/dbfile.txt', 'r')
        counter = 0 
        rdbfile = dbfile.read()
        nline = rdbfile.split('\n')
        print('lenline:',len(nline))
        for i in nline:
            if i:
                counter += 1
        
        # print(dict,counter+1)

        

        print(nline[counter-1], counter)
        print('End Storage Func')
        
        

    def submit():
        i = 0
        i += 1
        gentry1 = entry1.get()
        gentry2 = entry2.get()
        gentry5 = entry5.get()
        gentry3 = entry3.get()
        gentry6 = entry6.get()
        gentry7 = entry7.get()
        gentry = [gentry1,gentry2,gentry5,gentry3,gentry6,gentry7,res_d,res_t]

        y = []
        dict = {
            i : y + gentry
        }

        storage(gentry)

        print(dict)
        # print(res_t[1])

    but4 = Button(newFrame, text='Submit Confirmation', command=submit)
    but4.pack(pady=10)

    newFrame.pack()


but1 = Button(root, text='Make a Reservation', command=reserve)
but1.pack()


but2 = Button(root, text='View Guest Records')
but2.pack()

but3 = Button(root, text='Finances')
but3.pack()


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)

# #use the tuple() function to display a readable version of the result:

# print(tuple(x))
# print(dict(zip(x)))

root.mainloop()