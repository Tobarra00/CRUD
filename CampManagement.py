from tkinter import *
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
import sqlite3


# Declaring the root of the interface as well as some configuration

root = Tk()
root.title("Camp Data Manager")
root.iconbitmap("CampIcon.ico")
root.resizable(False, False)

# ---------------- Funtionalities --------------------

def create_db():
    '''
    This function creates a database with the desired name. In case the name already exists,
    it shows an error and nothing is created.   
    
    '''
    data_base_name = ""
    while data_base_name == "":
        data_base_name = simpledialog.askstring("Camp", "Introduce a database name: \t\t")
        if data_base_name == "":
            messagebox.showwarning("Camp", "Name of the database can't be empty.")
    
    # This if statment is included because pressing "Cancel" or the "X" button of the simpledialog.askstring module returns None.        
    if data_base_name != None:         
        db_connexion = sqlite3.connect(f"{data_base_name}.db")
        db_cursor = db_connexion.cursor()
        try:
            db_cursor.execute('''CREATE TABLE CAMPINFO(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        NAME VARCHAR(20),
                                                        SURNAME VARCHAR(50), 
                                                        BIRTH_DATE VARCHAR(10),
                                                        COMMENTS VARCHAR(200))''')
            
            messagebox.showinfo("Camp", "Data base created sucessfully.")
            
        except sqlite3.OperationalError:
            messagebox.showerror("Camp", "Database already exists.")
        
        db_connexion.close()
    
    
def exit_app():
    '''
    This function shows a message box letting asking if you are sure about exiting the app
    '''
    
    exit_answer = messagebox.askyesno("Camp", "Are you sure you want to exit the program?")
    if exit_answer:
        root.quit()


# Adding a menu to the root

main_menu = Menu(root)
root.config(menu=main_menu)

data_base_menu = Menu(main_menu, tearoff=0)
data_base_menu.add_command(label="Create Data Base", command=create_db)
data_base_menu.add_command(label="Open Data Base")
data_base_menu.add_separator()
data_base_menu.add_command(label="Exit", command=exit_app)

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