#!/usr/bin/python3

from tkinter import *
import _thread
import time
from PIL import Image, ImageTk


def get_dates():
	sDay = Start_Day.get()
	sMonth = Start_Month.get()
	sYear = Start_Year.get()
	eDay = End_Day.get()
	eMonth = End_Month.get()
	eYear = End_Year.get()
	
	print ("Starting Date: " + str(sDay) + '/' + str(sMonth) + '/' + str(sYear) )
	print ("Ending Date : " + str(eDay) + '/' + str(eMonth) + '/' + str(eYear) )
	print ("")

def press_up1(event):
	num = Start_Day.get()
	Start_Day.delete(0, END)
	Start_Day.insert(0, int(num) + 1 )
	print("Num: " + str( Start_Day.get() ) )
	print("pressed up1")

def press_minus1(event):
	num = Start_Day.get()
	Start_Day.delete(0, END)
	Start_Day.insert(0, int(num) - 1 )
	print("Num: " + str( Start_Day.get() ) )
	print("Pressed Minus1")


	
def press_up2(event):
	num = Start_Month.get()
	Start_Month.delete(0, END)
	Start_Month.insert(0, int(num) + 1 )
	print("Num: " + str( Start_Month.get() ) )
	print("pressed up2")

def press_minus2(event):
	num = Start_Month.get()
	Start_Month.delete(0, END)
	Start_Month.insert(0, int(num) - 1 )
	print("Num: " + str( Start_Month.get() ) )
	print("Pressed Minus2")


	
def press_up3(event):
	num = Start_Year.get()
	Start_Year.delete(0, END)
	Start_Year.insert(0, int(num) + 1 )
	print("Num: " + str( Start_Day.get() ) )
	print("pressed up3")

def press_minus3(event):
	num = Start_Year.get()
	Start_Year.delete(0, END)
	Start_Year.insert(0, int(num) - 1 )
	print("Num: " + str( Start_Year.get() ) )
	print("Pressed Minus3")



def press_up4(event):
	num = End_Day.get()
	End_Day.delete(0, END)
	End_Day.insert(0, int(num) + 1 )
	print("Num: " + str( End_Day.get() ) )
	print("pressed up4")

def press_minus4(event):
	num = End_Day.get()
	End_Day.delete(0, END)
	End_Day.insert(0, int(num) - 1 )
	print("Num: " + str( End_Day.get() ) )
	print("Pressed Minus4")


	
def press_up5(event):
	num = End_Month.get()
	End_Month.delete(0, END)
	End_Month.insert(0, int(num) + 1 )
	print("Num: " + str( End_Month.get() ) )
	print("pressed up5")

def press_minus5(event):
	num = End_Month.get()
	End_Month.delete(0, END)
	End_Month.insert(0, int(num) - 1 )
	print("Num: " + str( End_Month.get() ) )
	print("Pressed Minus5")



	
def press_up6(event):
	num = End_Year.get()
	End_Year.delete(0, END)
	End_Year.insert(0, int(num) + 1 )
	print("Num: " + str( End_Year.get() ) )
	print("pressed up6")

def press_minus6(event):
	num = End_Year.get()
	End_Year.delete(0, END)
	End_Year.insert(0, int(num) - 1 )
	print("Num: " + str( End_Year.get() ) )
	print("Pressed Minus6")


def CheckValid( threadName, delay):
        while 1:
                if int( Start_Day.get() ) > 31 or int (Start_Day.get()) <0:
                        Start_Day.delete(0, END)
                        Start_Day.insert(END, 15)
                        print ("You entered an invalid date")
                if int( End_Day.get() ) > 31 or int (End_Day.get()) <0:
                        End_Day.delete(0, END)
                        End_Day.insert(END, 25)
                        print ("You entered an invalid date")

                        
                if int (Start_Month.get()) > 12 or int (Start_Month.get()) < 0:
                        Start_Month.delete(0, END)
                        Start_Month.insert(END, 5)
                        print ("You entered an invalid date")
                if int (End_Month.get()) > 12 or int (End_Month.get()) < 0:
                        End_Month.delete(0, END)
                        End_Month.insert(END, 12)
                        print ("You entered an invalid date")


                if int (Start_Year.get()) > 2050 or int (Start_Year.get()) < 2016:
                        Start_Year.delete(0, END)
                        Start_Year.insert(END, 2016)
                        print ("You entered an invalid date")
                if int (End_Year.get()) > 2050 or int (End_Year.get()) < 2016:
                        End_Year.delete(0, END)
                        End_Year.insert(END, 2016)
                        print ("You entered an invalid date")
                 
                time.sleep(0.5)
                


#Setting up Window
master = Tk()
master.geometry("480x320")

Label(master, justify = CENTER, text="Start Date").grid(row = 0, column = 0, columnspan = 3)

#Creating Labels 
Label(master, justify = CENTER, text="Day").grid(row = 2, column = 0)
Label(master, justify = CENTER, text="Month").grid(row = 2, column = 3)
Label(master, justify = CENTER, text="Year").grid(row = 2, column = 6)



#Creating Text Boxes and buttons

Start_Day = Entry(master, font = (12), width = (4))
Start_Day.grid(row = 3, column = 0, rowspan = 2 )
Start_Day.insert(END, 28)

photo_up1 = PhotoImage(file = "images/plus.gif")
up1 = Button(master, image = photo_up1, )#command = increment(spot))
up1.grid(row = 3, column = 1, columnspan = 2)
up1.bind("<Button-1>", press_up1)

photo_minus1 = PhotoImage(file = "images/minus.gif")
minus1 = Button(master, image = photo_minus1, )#command = increment(spot))
minus1.grid(row = 4, column = 1, columnspan = 2)
minus1.bind("<Button-1>", press_minus1)




Start_Month = Entry(master, font = (12), width = (4)  )
Start_Month.grid(row = 3, column = 3, rowspan = 2)
Start_Month.insert(END, 5)

photo_up2 = PhotoImage(file = "images/plus.gif")
up2 = Button(master, image = photo_up2, )#command = increment(spot))
up2.grid(row = 3, column = 4, columnspan = 2, )
up2.bind("<Button-1>", press_up2)

photo_minus2 = PhotoImage(file = "images/minus.gif")
minus2 = Button(master, image = photo_minus2, )#command = increment(spot))
minus2.grid(row = 4, column = 4, columnspan = 2)
minus2.bind("<Button-1>", press_minus2)



Start_Year = Entry(master, font = (12), width = (4))
Start_Year.grid(row = 3, column = 6, rowspan=2)
Start_Year.insert(END, 2016)

photo_up3 = PhotoImage(file = "images/plus.gif")
up3 = Button(master, image = photo_up3, )#command = increment(spot))
up3.grid(row = 3, column = 7, columnspan = 2)
up3.bind("<Button-1>", press_up3)

photo_minus3 = PhotoImage(file = "images/minus.gif")
minus3 = Button(master, image = photo_minus3, )#command = increment(spot))
minus3.grid(row = 4, column = 7, columnspan = 2)
minus3.bind("<Button-1>", press_minus3)



#Label(master, justify = CENTER, text="End Date").grid(row = 8, column = 0, columnspan = 3)

#Creating the Labels
#Label(master, justify = CENTER, text="Month").grid(row = 10, column = 0)
#Label(master, justify = CENTER, text="Day").grid(row = 10, column = 1)
#Label(master, justify = CENTER, text="Year").grid(row = 10, column = 2)



#Creating and setting defaults for End Dates

End_Day = Entry(master, font = (12), width = (4))
End_Day.grid(row = 6, column = 0, rowspan = 2)
End_Day.insert(END, 25)

photo_up4 = PhotoImage(file = "images/plus.gif")
up4 = Button(master, image = photo_up4, )#command = increment(spot))
up4.grid(row = 6, column = 1, columnspan = 2)
up4.bind("<Button-1>", press_up4)

photo_minus4 = PhotoImage(file = "images/minus.gif")
minus4 = Button(master, image = photo_minus4, )#command = increment(spot))
minus4.grid(row = 7, column = 1, columnspan = 2)
minus4.bind("<Button-1>", press_minus4)



End_Month = Entry(master, font = (12), width = (4))
End_Month.insert(END, 12)
End_Month.grid(row = 6, column = 3, rowspan = 2)

photo_up5 = PhotoImage(file = "images/plus.gif")
up5 = Button(master, image = photo_up5, )#command = increment(spot))
up5.grid(row = 6, column = 4, columnspan = 2)
up5.bind("<Button-1>", press_up5)

photo_minus5 = PhotoImage(file = "images/minus.gif")
minus5 = Button(master, image = photo_minus5, )#command = increment(spot))
minus5.grid(row = 7, column = 4, columnspan = 2)
minus5.bind("<Button-1>", press_minus5)




End_Year = Entry(master, font = (12), width = (4))
End_Year.grid(row = 6, column = 6, rowspan = 2)
End_Year.insert(END, Start_Year.get())

photo_up6 = PhotoImage(file = "images/plus.gif")
up6 = Button(master, image = photo_up6, )#command = increment(spot))
up6.grid(row = 6, column = 7, columnspan = 2)
up6.bind("<Button-1>", press_up6)

photo_minus6 = PhotoImage(file = "images/minus.gif")
minus6 = Button(master, image = photo_minus6, )#command = increment(spot))
minus6.grid(row = 7, column = 7, columnspan = 2)
minus6.bind("<Button-1>", press_minus6)



Button(master, text = "Submit", command = get_dates).grid(row = 13, column = 0, columnspan = 3)

#Creating the checkButtons for Music play hours

Label(master, text="AM - Music - Hours").grid(row = 8, column = 7, columnspan = 8)
for i in range(0, 12):
	var = IntVar()
	c = Checkbutton(master, text="", variable=var )
	c.grid(row = 9, column = i)
	if i == 0:
		Label(master, justify = CENTER, text=str(12)).grid(row = 8, column = i)
	else:
		Label(master, justify = CENTER, text=str(i)).grid(row = 8, column = i)





#Button(master, text="", command=increment(spot)).grid(row = 11, column = 7, columnspan = 9)

_thread.start_new_thread( CheckValid, ("Thread-2", 1, ) )



master.mainloop()



















