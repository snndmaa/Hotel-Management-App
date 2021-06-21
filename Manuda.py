from tkinter import *
import tkinter.messagebox
import datetime
from pickle import *
from pymongo import MongoClient
import pandas as pd
from pandastable import Table


client = MongoClient('localhost', 27017)
thedb = client['hoteldb']
newcol = thedb['guests']
dblist = client.list_database_names()
print('Software Started.'+'Database Initialized')


root = Tk()
root.configure(background='lightblue')
root.title('Manuda Hotel Manager')
root.geometry('1500x900')

Topic = Label(root, text='Select an Option to get Started', font=('Arial', 35))
Topic.pack(fill=X, pady=150)

def reserve():
    newWindow = tkinter.Toplevel(root)
    newWindow.configure(background='lightblue')
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

        # print(see_db)
        # print('End Storage Func')
        

    def d_format(e1, d, e2):
        try:
            date_obj = datetime.datetime.strptime(e1, d)
            date_obj2 = datetime.datetime.strptime(e2, d)
            print(date_obj2)
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
        gentry = {'Full Name: ': gentry1, 'Arrival Date: ': gentry2, 'Departure Date: ': gentry5, 'Phone Number: ': gentry3, 'Room Number/Price: ': gentry6, 'Staff Name: ': gentry7, 'Date': res_d, 'Time': res_t}
        date_format = '%d/%m/%Y'
        
        d_format(gentry2, date_format, gentry5)

        if(gentry1 == '' or gentry2 == '' or gentry3 == '' or gentry5 == '' or gentry6 == '' or gentry7 == ''):
            mes1 = tkinter.messagebox.showerror(title='Empty Entry', message='Please ensure all form fields are filled in order to successfully book a reservation.')
            mes1.pack()
        elif(gentry2 == gentry5 or type(gentry1) == int or len(gentry3) != 11 or type(gentry7) == int):
            mes2 = tkinter.messagebox.showerror(title='Your Entry contains the Following Errors:', message='- Departure and Arrival Dates cannot be the same''\n'
            '- Name cannot contain a Number.''\n'
            '- Date Must be written in Correct Format.''\n'
            '- Phone Number must be 11 DIGITS')
            mes2.pack()

        else:
            if tkinter.messagebox.askokcancel('Confirmation', 'Do you wish to Submit'):
                storage(gentry)
                newWindow.destroy()
            else:
                u = 'Class'


        
        # print(res_t[1])
        u2 = 'Class'

    but4 = Button(newFrame, text='Submit Confirmation', command=submit, activebackground='lightgreen', width=40)
    but4.pack(pady=10)

    newFrame.pack()


but1 = Button(root, text='Make a Reservation', command=reserve, activebackground='orangered', width=40)
but1.pack()


def record():
    inventory_data = [data for data in newcol.find({}, {'_id':0})]
    df_inventory_data = pd.DataFrame(inventory_data)
    
    rec_window = tkinter.Toplevel(root)
    rec_window.title('Guest Database')
    rec_window.geometry('1110x600')

    pt = Table(rec_window, dataframe=df_inventory_data)
    pt.show()

    # print('End of Record func!')

but2 = Button(root, text='View Guest Records', command=record, activebackground='orangered', width=40)
but2.pack()

def soon():
    newWindow = tkinter.Toplevel(root)
    newWindow.configure(background='lightblue')
    newWindow.title('Loading')
    newWindow.geometry('470x250')

    newFrame = Frame(newWindow)
    info = Label(newFrame, text='Premium Feature. Coming soon.', font=('Arial', 15))
    info.pack(pady=40)
    newFrame.pack()



but3 = Button(root, text='Finance Management', command=soon, activebackground='orangered', width=40)
but3.pack()


def cleardb():
    newWindow = tkinter.Toplevel(root)
    newWindow.configure(background='lightblue')
    newWindow.title('Admin Confirmation')
    newWindow.geometry('670x250')

    newFrame = Frame(newWindow)


    info = Label(newFrame, text='Please Enter Admin Password to perform this action.', font=('Arial', 15))
    entry8 = Entry(newFrame, textvariable=StringVar, width='50', bg='lightyellow', cursor='dot')


    info.pack(pady=40)
    entry8.pack()


    

    
    # delcol = newcol.delete_many({}) 
    # print(delcol.deleted_count, " documents deleted.")

    def pasval():
        gentry8 = entry8.get()
        if(gentry8 == 'havana01'):
            delcol = newcol.delete_many({})
            delnum = delcol.deleted_count
            tkinter.messagebox.showinfo(title='Password Correct', message='DataBase has been cleared of '+ str(delnum)+ ' Entries')
            newWindow.destroy()

        else:
            tkinter.messagebox.showwarning(title='Incorrect Password', message='Please desist from trying if you are not Admin')
            newWindow.destroy()

    but6 = Button(newFrame, text='Confirm', command=pasval, activebackground='orangered', width=40)
    but6.pack()

    newFrame.pack()


but5 = Button(root, text='Clear Database', command=cleardb, activebackground='orangered', width=40)
but5.pack()


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)

# #use the tuple() function to display a readable version of the result:

# print(tuple(x))
# print(dict(zip(x)))


root.mainloop()