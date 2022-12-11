from tkinter import *

#its only one line entry

def temp(e):
    entry.delete(0,"end")
    entry.config(show = '*')

root = Tk()

#width is number of characters
#it doesnt control the number of input, just how it looks
entry = Entry(root, width=30)

#get content
entry.get()

#delete content
entry.delete(0, END)

#insert content
entry.insert(0, 'enter your password')

#how text is being shown
#entry.config(show = '*')

#we can use ttk to disable and enable the entry widget
#entry.state(['disabled'])

#example of binding event.
entry.bind("<FocusIn>",temp)


entry.pack()

root.mainloop()