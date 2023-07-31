from tkinter import messagebox
import tkinter as tk
import webbrowser


def how_to_use():
    messagebox.showinfo("Camp info", "This is a quick guide on how to use this C.R.U.D application.")

def about():

    about_info = tk.Toplevel()
    about_info.title("About")
    about_info.geometry("500x150")
    about_info.resizable(False, False)

    info = "This is a personal project to practice how to perform the C.R.U.D process. With this app, you should be able to create, read, update and delete entries from a database, which you can open or create. I have tried to put attentions to the details so that there are the least posible amount of bugs.\n\nYou can see more in the following link:"
    link = "https://github.com/Tobarra00"

    info_label = tk.Label(about_info, text=info, wraplength=400, justify="center")
    info_label.pack()

    link_label = tk.Label(about_info, text=link, fg="blue", cursor="hand2")
    link_label.pack()

    def open_link(event):
        webbrowser.open(link)

    link_label.bind("<Button-1>", open_link)

    about_info.mainloop()