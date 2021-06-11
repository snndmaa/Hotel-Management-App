from tkinter import *
import tkinter.messagebox
import datetime
from pickle import *
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
thedb = client['hoteldb']
newcol = thedb['guests']
dblist = client.list_database_names()
print('DB Names: ', dblist)

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
    nom = Label(newFrame, text=' Full Name', font=('Arial', 20))
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
    res_d = str(res_dt.day)+'/'+ str(res_dt.month)+'/'+ str(res_dt.year)
    res_t = str(res_dt.hour)+':'+ str(res_dt.minute)

    def storage(dict): 
        insert_db = newcol.insert_one(dict)
        see_db = newcol.find()

        print(see_db)
        print('End Storage Func')
        

    def d_format(e, d):
        try:
            date_obj = datetime.datetime.strptime(e, d)
            print(date_obj)
        except ValueError:
            tkinter.messagebox.showerror(title='Date Error', message='Incorrect data format, should be DD/MM/YYY')        
    

    def submit():
        i = 0
        i += 1
        gentry1 = entry1.get()
        gentry2 = entry2.get()
        gentry5 = entry5.get()
        gentry3 = entry3.get()
        gentry6 = entry6.get()
        gentry7 = entry7.get()
        gentry = {'Full Name: ': gentry1, 'Arrival Date: ': gentry2, 'Departure Date: ': gentry5, 'Phone Number: ': gentry3, 'Room Number/Price: ': gentry6, 'Staff Name: ': gentry7, 'Auto_Date': res_d, 'Auto_Time': res_t}
        date_format = '%d/%m/%Y'
        
        d_format(gentry2, date_format)

        if(gentry1 == '' or gentry2 == '' or gentry3 == '' or gentry5 == '' or gentry6 == '' or gentry7 == ''):
            mes1 = tkinter.messagebox.showerror(title='Empty Entry', message='Please ensure all form fields are filled in order to successfully book a reservation.')
            mes1.pack()
        elif(gentry2 == gentry5 or type(gentry1) == int ):
            mes2 = tkinter.messagebox.showerror(title='Your Entry contains the Following Errors:', message='- Departure and Arrival Dates cannot be the same''\n'
            '- Name cannot contain a Number.''\n'
            '- ')
            mes2.pack()

        else:
            storage(gentry)


        
        # print(res_t[1])

    but4 = Button(newFrame, text='Submit Confirmation', command=submit)
    but4.pack(pady=10)

    newFrame.pack()


but1 = Button(root, text='Make a Reservation', command=reserve)
but1.pack()


def record():
    with open('C://Users/USER/Desktop/freelance/py/tkinter/dbfile.txt', 'r') as dict_items_open:
        BDICT = dict_items_open
        firstrunDICT = False
        print(BDICT)
        print('End of Record func!')


but2 = Button(root, text='View Guest Records', command=record)
but2.pack()

but3 = Button(root, text='Finances')
but3.pack()

def cleardb():
    delcol = newcol.delete_many({}) 
    print(delcol.deleted_count, " documents deleted.")

but5 = Button(root, text='Clear Database', command=cleardb)
but5.pack()


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)

# #use the tuple() function to display a readable version of the result:

# print(tuple(x))
# print(dict(zip(x)))


root.mainloop()