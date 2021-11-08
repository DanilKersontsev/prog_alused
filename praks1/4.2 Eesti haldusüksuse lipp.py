from tkinter import *
raam = Tk()
raam.title("Karksi valla lipp")
tahvel = Canvas(raam, width = 900, height = 700)
tahvel.create_rectangle(0, 0, 900, 300, fill="gold")
tahvel.create_rectangle(0, 300, 900, 400, fill="white")
tahvel.create_rectangle(0, 400, 900, 900, fill="darkcyan")
tahvel.pack()
raam.mainloop()