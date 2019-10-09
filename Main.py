from tkinter import *
from Info import Info

def set_position_menu2():
    lbCounter.place(x=60,y=50)

def set_position_menu1():
    inputDoors.place(x=100, y=0)
    inputGift.place(x=100, y=20)
    inputRepetitions.place(x=100, y=40)
    lbDoors.place(x=0, y=0)
    lbGift.place(x=0, y=20)
    lbRepetitions.place(x=0, y=40)

def visible_menu2():
    if lbCounter.winfo_viewable():
        lbCounter.place_forget()
    else :
        set_position_menu2()

def visible_menu1():
    if lbRepetitions.winfo_viewable():
        lbRepetitions.place_forget()
        lbDoors.place_forget()
        lbGift.place_forget()
        inputDoors.place_forget()
        inputRepetitions.place_forget()
        inputGift.place_forget()
    else :
        set_position_menu1()
    visible_menu2()

def start():
    info = Info(inputDoors.get(), inputGift.get(), inputRepetitions.get())
    visible_menu1()

root = Tk()
root.title("Monte Carlo")
root.geometry("600x400+450+100")

lbDoors = Label(text="Doors")
lbGift = Label(text="Gifts")
lbRepetitions = Label(text="Repetitions")
lbCounter = Label(text="Counter")

inputDoors = Entry()
inputGift = Entry()
inputRepetitions = Entry()

butStart = Button(root, text='Start', command=start)
butStart.place(x=300, y=200)
inputDoors.place(x=100, y=0)
inputGift.place(x=100, y=20)
inputRepetitions.place(x=100, y=40)

lbDoors.place(x=0, y=0)
lbGift.place(x=0, y=20)
lbRepetitions.place(x=0, y=40)

root.mainloop()
