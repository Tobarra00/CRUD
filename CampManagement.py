from tkinter import *
from tkinter import scrolledtext, filedialog
import FileFunctionalities as FF


# Declaring the root of the interface as well as some configuration

root = Tk()
root.title("Camp Data Manager")
root.iconbitmap("CampIcon.ico")
root.resizable(False, False)

# Adding a menu to the root

main_menu = Menu(root)
root.config(menu=main_menu)

data_base_menu = Menu(main_menu, tearoff=0)
data_base_menu.add_command(label="Create Database", command=FF.create_db)
data_base_menu.add_command(label="Open Database")
data_base_menu.add_separator()
data_base_menu.add_command(label="Exit", command=lambda:FF.exit_app(root))

clear_data_menu = Menu(main_menu, tearoff=0)
clear_data_menu.add_command(label="Clear info")

crud_menu = Menu(main_menu, tearoff=0)
crud_menu.add_command(label="Create")
crud_menu.add_command(label="Read")
crud_menu.add_command(label="Update")
crud_menu.add_command(label="Delete")

info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label="How to use")
info_menu.add_command(label="About")

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


# Adding buttons at the bottom of the interface to performe C.R.U.D.
create_button = Button(my_frame, text="Create", height=1, width=10)
create_button.grid(row=6, column=0, padx=5, pady=10)

read_button = Button(my_frame, text="Read", height=1, width=10)
read_button.grid(row=6, column=1, padx=5, pady=10)

update_button = Button(my_frame, text="Update", height=1, width=10)
update_button.grid(row=6, column=2, padx=5, pady=10)

delete_button = Button(my_frame, text="Delete", height=1, width=10)
delete_button.grid(row=6, column=3, padx=5, pady=10)


# Mainloop to continuously run the application
root.mainloop()