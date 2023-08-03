from tkinter import Toplevel, Label
import webbrowser


def how_to_use():
    how_to_use = Toplevel()
    how_to_use.title("How to use")
    how_to_use.geometry("600x400")
    how_to_use.iconbitmap("CampIcon.ico")
    how_to_use.resizable(False, False)
    how_to_use_info = "This window shows a step by step guide on how to use this program. It is designed to work with a database and be able to perform C.R.U.D. operations:\n\n1. First step is to create or open a database. Without a connection, the program won't work. Go to 'File' and choose an option.\n\n2. Once you have created/opened a valid database, you can start by creating a new user or if the database already contains info, you can search, read, update or delete the info.\n\n3. To create a user you will have to fill the the gaps with the name, surname, birth date and some comments and then press the create button.\n\n4. Once the user is created, you can read the info, update it or delete it. For it, you will have to introduce the id of the user you want to interact with and then press the action you want to perform. After permorfing the action, you can clear the info in the screen pressing the 'Clear info' menu. You can know the id of a user by knowing the order in which they were created, or you can just introduce the user name in the search bar, which will return you the id of the user so you can later introduce it in the id field to perform any of the 3 operations mentioned before.\n\n5. And that's all, with this info you should be able to manage a database and perform C.R.U.D. operations."
    htu_info_label = Label(how_to_use, text=how_to_use_info, justify="left", wraplength=550)
    htu_info_label.grid(padx=20, pady=20)
    
    how_to_use.mainloop()

def about():

    about_info = Toplevel()
    about_info.title("About...")
    about_info.geometry("500x150")
    about_info.iconbitmap("CampIcon.ico")
    about_info.resizable(False, False)

    info = "This is a personal project to practice how to perform the C.R.U.D process. With this app, you should be able to create, read, update and delete entries from a database, which you can open or create. I have tried to put attentions to the details so that there are the least posible amount of bugs.\n\nYou can see more in the following link:"
    link = "https://github.com/Tobarra00"

    info_label = Label(about_info, text=info, wraplength=400, justify="center")
    info_label.pack()

    link_label = Label(about_info, text=link, fg="blue", cursor="hand2")
    link_label.pack()

    def open_link(event):
        webbrowser.open(link)

    link_label.bind("<Button-1>", open_link)

    about_info.mainloop()