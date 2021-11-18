from tkinter import *
raam = Tk()
raam.title("Liiklusmärk")
tahvel = Canvas(raam,width=600, height =600)
tahvel.create_oval(10,10,600,600, fill="red", outline="black")
tahvel.create_rectangle(500,360,560,240, fill="white", outline="white")
tahvel.pack()
raam.mainloop()
