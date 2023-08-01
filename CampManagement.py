from tkinter import *
from tkinter import scrolledtext
import FileFunctionalities as FF
import AppInformation as AppInfo


# Declaring the root of the interface as well as some configuration
root = Tk()
root.title("Camp Data Manager")
root.iconbitmap("CampIcon.ico")
root.resizable(False, False)

# Creating the connection to the data base
connect = FF.DbConection()

# These are the variables that will be send to the DB
id = StringVar()
name = StringVar()
surname = StringVar()
birth_date = StringVar()

# Adding a menu to the root
main_menu = Menu(root)
root.config(menu=main_menu)

data_base_menu = Menu(main_menu, tearoff=0)
data_base_menu.add_command(label="Create Database", command=connect.create_db)
data_base_menu.add_command(label="Open Database", command=connect.open_db)
data_base_menu.add_separator()
data_base_menu.add_command(label="Exit", command=lambda:connect.exit_app(root))

clear_data_menu = Menu(main_menu, tearoff=0)
clear_data_menu.add_command(label="Clear info", command=lambda:connect.clear_info(id, name, surname, birth_date, comments_entry))

crud_menu = Menu(main_menu, tearoff=0)
crud_menu.add_command(label="Create", command=lambda:connect.create_entry(name, surname, birth_date, comments_entry))
crud_menu.add_command(label="Read", command=lambda:connect.read_entry(id, name, surname, birth_date, comments_entry))
crud_menu.add_command(label="Update", command=lambda:connect.update_entry(id, name, surname, birth_date, comments_entry))
crud_menu.add_command(label="Delete", command=lambda:connect.delete_entry(id))

info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label="How to use", command=AppInfo.how_to_use)
info_menu.add_command(label="About...", command=AppInfo.about)

main_menu.add_cascade(label="File", menu=data_base_menu)
main_menu.add_cascade(label="Clear data", menu=clear_data_menu)
main_menu.add_cascade(label="CRUD", menu=crud_menu)
main_menu.add_cascade(label="Info", menu=info_menu)


# Create a Frame 
my_frame = Frame(root, height=300, width=300)
my_frame.pack()

# Adding text labels to the fields
id_label = Label(my_frame, text="ID")
id_label.grid(row=1, column=0, padx=3, pady=4)
name_label = Label(my_frame, text="Name")
name_label.grid(row=2, column=0, padx=3, pady=4)
surname_label = Label(my_frame, text="Surname")
surname_label.grid(row=3, column=0, padx=3, pady=4)
birth_date_label = Label(my_frame, text="Birth Date")
birth_date_label.grid(row=4, column=0, padx=3, pady=4)
comments_label = Label(my_frame, text="Comments")
comments_label.grid(row=5, column=0, padx=3, pady=4)


# Adding text input entries to the fields
id_entry = Entry(my_frame, width=40, textvariable=id)
id_entry.grid(row=1, column=1, columnspan=3, padx=3, pady=4)
name_entry = Entry(my_frame, width=40, textvariable=name)
name_entry.grid(row=2, column=1, columnspan=3, padx=3, pady=4)
surname_entry = Entry(my_frame, width=40, textvariable=surname)
surname_entry.grid(row=3, column=1, columnspan=3, padx=3, pady=4)
birth_date_entry = Entry(my_frame, width=40, textvariable=birth_date)
birth_date_entry.grid(row=4, column=1, columnspan=3, padx=3, pady=4)
comments_entry = scrolledtext.ScrolledText(my_frame)
comments_entry.grid(row=5, column=1, columnspan=3, padx=3, pady=4)
comments_entry.config(width=28, height=4)


# Adding buttons at the bottom of the interface to performe C.R.U.D.
create_button = Button(my_frame, text="Create", height=1, width=10, command=lambda:connect.create_entry(name, surname, birth_date, comments_entry))
create_button.grid(row=6, column=0, padx=5, pady=10)
read_button = Button(my_frame, text="Read", height=1, width=10, command=lambda:connect.read_entry(id, name, surname, birth_date, comments_entry))
read_button.grid(row=6, column=1, padx=5, pady=10)
update_button = Button(my_frame, text="Update", height=1, width=10, command=lambda:connect.update_entry(id, name, surname, birth_date, comments_entry))
update_button.grid(row=6, column=2, padx=5, pady=10)
delete_button = Button(my_frame, text="Delete", height=1, width=10, command=lambda:connect.delete_entry(id))
delete_button.grid(row=6, column=3, padx=5, pady=10)

root.bind("<Destroy>", lambda event:connect.exit_x)

# Mainloop to continuously run the application
root.mainloop()