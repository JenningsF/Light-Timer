#!/usr/bin/python3

from tkinter import *
#from Pillow import *
from PIL import Image, ImageTk

def get_dates():
	date1 = Start_Month.get()
	print (date1)

#Setting up Window
master = Tk()
master.geometry("480x320")

Label(master, justify = CENTER, text="Start Date").grid(row = 0, column = 0, columnspan = 3)

#Creating Labels 
Label(master, justify = CENTER, text="Month").grid(row = 2, column = 0)
Label(master, justify = CENTER, text="Day").grid(row = 2, column = 1)
Label(master, justify = CENTER, text="Year").grid(row = 2, column = 2)

#Creating Starting Dates
Start_Month = Entry(master, font = (12), width = (4))
Start_Month.grid(row = 3, column = 0)
Start_Month.insert(END, 5)

Start_Day = Entry(master, font = (12), width = (4))
Start_Day.grid(row = 3, column = 1)
Start_Day.insert(END, 5)

Start_Year = Entry(master, font = (12), width = (6))
Start_Year.grid(row = 3, column = 2)
Start_Year.insert(END, 2016)


Label(master, justify = CENTER, text="End Date").grid(row = 8, column = 0, columnspan = 3)

#Creating the Labels
Label(master, justify = CENTER, text="Month").grid(row = 10, column = 0)
Label(master, justify = CENTER, text="Day").grid(row = 10, column = 1)
Label(master, justify = CENTER, text="Year").grid(row = 10, column = 2)

#Creating and setting defaults for End Dates
End_Month = Entry(master, font = (12), width = (4))
End_Month.insert(END, 12)
End_Month.grid(row = 11, column = 0)

End_Day = Entry(master, font = (12), width = (4))
End_Day.grid(row = 11, column = 1)
End_Day.insert(END, 25)

End_Year = Entry(master, font = (12), width = (6))
End_Year.grid(row = 11, column = 2)
End_Year.insert(END, Start_Year.get())

Button(master, text = "Submit", command = get_dates).grid(row = 13, column = 0, columnspan = 3)

#Creating the checkButtons for Music play hours

Label(master, text="AM - Music - Hours").grid(row = 0, column = 7, columnspan = 8)
for i in range(0, 12):
        var = IntVar()
        c = Checkbutton(master, text="", variable=var )
        c.grid(row = 3, column = i+5)
        if i == 0:
                Label(master, justify = CENTER, text=str(12)).grid(row = 2, column = i+5)
        else:
                Label(master, justify = CENTER, text=str(i)).grid(row = 2, column = i+5)



#Creating the buttons that increment date
cursor = 0
def press_up(event):
        print("pressed up")

#Button(master, text="", command=increment(spot)).grid(row = 11, column = 7, columnspan = 9)

photo_up = PhotoImage(file = "images/up.gif")
up = Button(master, image = photo_up, )#command = increment(spot))
up.grid(row = 8, column = 9, columnspan = 5, rowspan = 5)
up.bind("<Button-1>", press_up)

photo_right = PhotoImage(file = "images/right.gif")
right = Button(master, image = photo_right, )#command = increment(spot))
right.grid(row = 11, column = 6, columnspan = 5, rowspan = 5)

photo_left = PhotoImage(file = "images/left.gif")
left = Button(master, image = photo_left, )#command = increment(spot))
left.grid(row = 11, column = 12, columnspan = 5, rowspan = 5)

photo_down = PhotoImage(file = "images/down.gif")
down = Button(master, image = photo_down, )#command = increment(spot))
down.grid(row = 13, column = 9, columnspan = 5, rowspan = 5)

master.mainloop()



















