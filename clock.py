# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# This function is used to
# display time on the label

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()

"""
from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('Python Clock')
Label(root,text = 'YOUTUBE - BUG NINZA', font ='arial 20 bold').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop()
"""