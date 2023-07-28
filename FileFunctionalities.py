import sqlite3
from tkinter import messagebox, simpledialog


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


def open_db():
    '''
    This function lets you open an existing database to work with it.
    '''
    
    pass    
    
def exit_app(tk_root):
    '''
    This function shows a message box letting asking if you are sure about exiting the app
    '''
    
    exit_answer = messagebox.askyesno("Camp", "Are you sure you want to exit the program?")
    if exit_answer:
        tk_root.quit()