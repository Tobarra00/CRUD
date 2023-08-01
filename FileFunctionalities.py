import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class DbConection():
    
    def __init__(self) -> None:
        self.db_connection = None
        self.db_cursor = None
        self.db_name = ""
    
    
    def create_db(self):
        '''
        This function creates a database with the desired name. In case the name already exists,
        it shows an error and nothing is created.   
        
        '''
        if self.db_connection:
            self.db_connection.close()
        self.db_name = ""
        while self.db_name == "":
            self.db_name = simpledialog.askstring("Camp", "Introduce a database name: \t\t")
            if self.db_name == "":
                messagebox.showwarning("Camp", "Name of the database can't be empty.")
        
        # This if statment is included because pressing "Cancel" or the "X" button of the simpledialog.askstring module returns None.        
        if self.db_name != None:         
            self.db_connection = sqlite3.connect(f"{self.db_name}.db")
            self.db_cursor = self.db_connection.cursor()
            try:
                self.db_cursor.execute('''CREATE TABLE CAMPINFO(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            NAME VARCHAR(20),
                                                            SURNAME VARCHAR(50), 
                                                            BIRTH_DATE VARCHAR(10),
                                                            COMMENTS VARCHAR(200))''')
                
                messagebox.showinfo("Camp", "Data base created sucessfully.")
                
            except sqlite3.OperationalError:
                messagebox.showerror("Camp", "Database already exists.")
            
            
    def open_db(self):
        '''
        This function lets you open an existing database to work with it.
        '''
        if self.db_connection:
            self.db_connection.close()
        self.db_name = filedialog.askopenfilename(title="Database Search", filetypes=(("", "*.db"),("Any file", "*.*")))
        self.db_connection = sqlite3.connect(self.db_name)
        self.db_cursor = self.db_connection.cursor()
        
    def exit_app(self, tk_root):
        '''
        This function shows a message box letting asking if you are sure about exiting the app
        '''
        exit_answer = messagebox.askyesno("Camp", "Are you sure you want to exit the program?")
        if exit_answer:
            if self.db_connection:
                self.db_connection.close()
            tk_root.quit()
    
    def exit_x(self):
        '''
        This function closes de open database. It is used when the "X" button is pressed.
        '''
        if self.db_connection:
                self.db_connection.close()
    
    def clear_info(self, *args):
        for fields in args:
            try:
                fields.set("")
            except AttributeError:
                fields.delete("1.0", tk.END)
                
    def create_entry(self, name, surname, birth_date, comments):
        '''
        This function creates a new element and is added to the database.
        '''
        self.db_cursor.execute(f"INSERT INTO CAMPINFO (name, surname, birth_date, comments) VALUES (?, ?, ?, ?)", (name.get(), surname.get(), birth_date.get(), comments.get('1.0', tk.END)))
        self.db_connection.commit()    
    
    def read_entry(self, id, name, surname, bith_date, comments):
        '''
        This function reads in the database the user assigned to the id you introduce
        '''
        self.db_cursor.execute(f"SELECT * FROM CAMPINFO WHERE ID=?", (id.get()))
        user_searched = self.db_cursor.fetchall()
        for user_info in user_searched:
            name.set(user_info[1])
            surname.set(user_info[2])
            bith_date.set(user_info[3])
            comments.delete("1.0", tk.END)
            comments.insert("1.0", user_info[4])
            
    def update_entry(self, id, name, surname, birth_date, comments):
        '''
        This function allows the user to modify any entry by introducing the id of the user you want to change
        '''
        self.db_cursor.execute("UPDATE CAMPINFO SET name=?, surname=?, birth_date=?, comments=? WHERE ID=?", (name.get(), surname.get(), birth_date.get(), comments.get('1.0', tk.END), id.get()))
        self.db_connection.commit()
        
    def delete_entry(self, id):
        '''
        This function allows the user to delete any entry based on the given id
        '''
        self.db_cursor.execute("DELETE FROM CAMPINFO WHERE ID=?", (id.get()))
        self.db_connection.commit()
        