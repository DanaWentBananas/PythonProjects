from tkinter import *
from tkinter import ttk

root = Tk()

#two progress bar modes: determinent, indeterminent

progress = ttk.Progressbar(root, orient=HORIZONTAL, length = 200)

#determinate mode
progress.config(mode = 'determinate', maximum = 10, value=3.3)

#jumps a step by 1, goes around when its full
#progress.step()

#indeterminate mode
#progress.config(mode = 'indeterminate')
#progress.start()
#progress.stop()

progress.pack()

root.mainloop()