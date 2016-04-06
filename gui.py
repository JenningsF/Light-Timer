#!/usr/bin/python3

from tkinter import *

def get_dates():
	start_month = start_month_entry.get()
	print (start_month)

master = Tk()
master.geometry("460x320")

Label(master, justify = CENTER, text="Start Date").grid(row = 0, column = 0, columnspan = 3)

Label(master, justify = CENTER, text="Month").grid(row = 2, column = 0)
Label(master, justify = CENTER, text="Day").grid(row = 2, column = 1)
Label(master, justify = CENTER, text="Year").grid(row = 2, column = 2)
start_month_entry = Entry(master, font = (12), width = (3))
start_month_entry.grid(row = 3, column = 0)
Entry(master, font = (12), width = (3)).grid(row = 3, column = 1)
Entry(master, font = (12), width = (4)).grid(row = 3, column = 2)


Label(master, justify = CENTER, text="End Date").grid(row = 8, column = 0, columnspan = 3)

Label(master, justify = CENTER, text="Month").grid(row = 10, column = 0)
Label(master, justify = CENTER, text="Day").grid(row = 10, column = 1)
Label(master, justify = CENTER, text="Year").grid(row = 10, column = 2)
Entry(master, font = (12), width = (3)).grid(row = 11, column = 0)
Entry(master, font = (12), width = (3)).grid(row = 11, column = 1)
Entry(master, font = (12), width = (4)).grid(row = 11, column = 2)

Button(master, text = "Submit", command = get_dates).grid(row = 13, column = 0, columnspan = 3)

master.mainloop()