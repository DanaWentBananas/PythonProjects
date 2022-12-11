from tkinter import *

root = Tk()

label = Label(root, text="hellolkeuwfhuwdehuewhfiuwehufhewufhjkew")
label.pack()

#wrap text
label.config(wraplength = 150)

#justify text
label.config(justify=CENTER)

#text color
label.config(foreground = 'blue')

#background color
label.config(background = 'yellow')

#font
label.config(font = ('Courier', 18, 'bold'))

#images
#can only use : gif, PGM/PPM
logo = PhotoImage(file = 'D:/LinkedIN/Tkinter/img.gif')
label.config(image = logo)

#gotta save a referance for debugging reasons
label.img = logo

#compound property
#bottom,top,center,left,right, none(default)
label.config(compound = 'right')


root.mainloop() 