from tkinter import *
from tkinter import simpledialog, scrolledtext, filedialog

root = Tk()
root.title("Camp Data Manager")
root.iconbitmap("CampIcon.ico")
root.resizable(False, False)

myFrame = Frame(root, height=300, width=300)
myFrame.pack()

idLabel = Label(myFrame, text="ID")
idLabel.grid(row=1, column=0, padx=3, pady=4)
name = Label(myFrame, text="Name")
name.grid(row=2, column=0, padx=3, pady=4)
surname = Label(myFrame, text="Surname")
surname.grid(row=3, column=0, padx=3, pady=4)
bDate = Label(myFrame, text="Birth Date")
bDate.grid(row=4, column=0, padx=3, pady=4)
comments = Label(myFrame, text="Comments")
comments.grid(row=5, column=0, padx=3, pady=4)

createButton = Button(myFrame, text="Create", height=1, width=10)
createButton.grid(row=6, column=0, padx=5, pady=10)
readButton = Button(myFrame, text="Read", height=1, width=10)
readButton.grid(row=6, column=1, padx=5, pady=10)
updateButton = Button(myFrame, text="Update", height=1, width=10)
updateButton.grid(row=6, column=2, padx=5, pady=10)
deleteButton = Button(myFrame, text="Delete", height=1, width=10)
deleteButton.grid(row=6, column=3, padx=5, pady=10)



root.mainloop()