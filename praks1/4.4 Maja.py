from tkinter import *
raam = Tk()
raam.title("Maja")
#Taust
tahvel = Canvas(raam, width=600, height = 600, background="skyblue")
#Muru
tahvel.create_rectangle(0,450,600,600, fill="green", outline="green")
#Maja
tahvel.create_rectangle(90,230,500,520, fill="goldenrod")
#Maja uks
tahvel.create_rectangle(120,390,180,500, fill="chocolate")
#maja ukse link
tahvel.create_line(160,460,170,460, width=2)

#Maja katus
tahvel.create_polygon(90,230,300,50,500,230, fill="grey",)
#Aken
tahvel.create_rectangle(430,450,350,370, fill="white", outline="black")
#aken sise osa


tahvel.pack()
raam.mainloop()