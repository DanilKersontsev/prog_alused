from easygui import *
input1 = integerbox("Sisestage esimene täisarv lõigus 1-10:")
input2 = integerbox("Sisestage teine täisarv lõigus 1-10:")
nupud = ["+", "-" , "*", "/"]
vajutati = buttonbox("Valige tehe", choices = nupud)

if vajutati == "+":
    summa = input1 + input2
elif vajutati == "-":
    summa = input1 - input2
elif vajutati == "*":
    summa = input1 * input2
elif vajutati == "/":
    summa = input1 // input2
input3 = msgbox("Tehte tulemus on " + str(summa))
