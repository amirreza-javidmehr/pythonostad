import backend
from tkinter import *

main = Tk()
main.title('training')

def select():
    connection = backend.check_connection()
    listData = backend.select_all_users(connection)
    myListbox.delete(0, END)
    for tupleItem in listData:
        # myListbox.insert(END, "\n")
        myListbox.insert(END, tupleItem)
        # for item in tupleItem:
        #     myListbox.insert(END, item)

def insert():
    name = nameEntry.get()
    lastname = lnameEntry.get()
    age = ageEntry.get()
    country = countryEntry.get()
    connection = backend.check_connection()
    backend.insert_into(connection, name, lastname, age, country)
    select()

def delete():
    name = nameEntry.get()
    connection = backend.check_connection()
    backend.delete_user(connection, name)
    select()


nameLabel = Label(main, text= 'name:')
nameLabel.grid(row=1, column=1)
nameEntry = Entry(main, width= 30)
nameEntry.grid(row=1, column=2)
lnameLabel = Label(main, text= 'last name:')
lnameLabel.grid(row=1, column=3)
lnameEntry = Entry(main, width= 30)
lnameEntry.grid(row=1, column=4)
ageLabel = Label(main, text= 'age:')
ageLabel.grid(row=2, column=1)
ageEntry = Entry(main, width= 30)
ageEntry.grid(row=2, column=2)
countryLabel = Label(main, text= 'country:')
countryLabel.grid(row=2, column=3)
countryEntry = Entry(main, width= 30)
countryEntry.grid(row=2, column=4)
myListbox = Listbox(main, width= 50, height= 30)
myListbox.grid(row=7, column=2)
myScrollbar = Scrollbar(main)
myScrollbar.grid(row=7, column=3)
myListbox.configure(yscrollcommand= myScrollbar.set)
myScrollbar.configure(command= myListbox.yview)
selectBtn = Button(main, text= 'Select', width= 20, command= select )
selectBtn.grid(row=3, column=4)
insertBtn = Button(main, text= 'Insert', width= 20, command= insert)
insertBtn.grid(row=4, column=4)
updateBtn = Button(main, text= 'Update', width= 20)
updateBtn.grid(row=5, column=4)
deleteBtn = Button(main, text= 'Delete', width= 20, command= delete)
deleteBtn.grid(row=6, column=4)

main.mainloop()