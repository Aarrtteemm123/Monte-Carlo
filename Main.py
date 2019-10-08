from tkinter import *

root = Tk()
root.title("Monte Carlo")
root.geometry("600x400+450+100")

lbDoors = Label(text="Doors")
lbPrices = Label(text="Prices")
lbRepetitions = Label(text="Repetitions")

inputDoors = Entry()
inputPrices = Entry()
inputRepetitions = Entry()

inputDoors.place(x=100,y=0)
inputPrices.place(x=100,y=20)
inputRepetitions.place(x=100,y=40)

lbDoors.place(x=0,y=0)
lbPrices.place(x=0,y=20)
lbRepetitions.place(x=0,y=40)

root.mainloop()