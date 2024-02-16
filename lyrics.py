# import modules
from tkinter import *
from lyrics_extractor import SongLyrics


# user defined function
def get_lyrics():
    extract_lyrics = SongLyrics(
        "AIzaSyDQj45RRxp4g5wJ3S4G4Vs-VVir-isT1P4", "b2068088a58c3401c")

    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    result.set(res)


# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='light grey')
#modifying

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song name : ",
      bg="light grey").grid(row=0, sticky=W)

Label(master, text="Result :",
      bg="light grey").grid(row=3, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result,
      bg="light grey").grid(row=3, column=1, sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

# creating a button using the widget
b = Button(master, text="Show",
           command=get_lyrics, bg="Blue")

b.grid(row=0, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5, )

mainloop()
