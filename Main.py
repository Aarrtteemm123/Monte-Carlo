from tkinter import *
from Info import Info

info = Info
counter = 0

def exit():
    root.destroy()

def set_position_menu2():
    lbCounter.place(x=240, y=80)
    butExit.place(x=260, y=250)
    left.place(x=20,y=130,width=280)
    right.place(x=300,y=130,width=280)
    lbDoors.place(x=240, y=20)
    lbGift.place(x=240, y=40)
    lbRepetitions.place(x=240, y=60)


def set_position_menu1():
    inputDoors.place(x=250, y=20)
    inputGift.place(x=250, y=40)
    inputRepetitions.place(x=250, y=60)
    lbDoors.place(x=180, y=20)
    lbGift.place(x=180, y=40)
    lbRepetitions.place(x=180, y=60)
    butStart.place(x=275, y=100)


def visible_menu2():
    if lbCounter.winfo_viewable():
        lbCounter.place_forget()
        butExit.place_forget()
        right.place_forget()
        left.place_forget()
    else:
        set_position_menu2()


def visible_menu1():
    if lbRepetitions.winfo_viewable():
        inputDoors.place_forget()
        inputRepetitions.place_forget()
        inputGift.place_forget()
        butStart.place_forget()
    else:
        set_position_menu1()
    visible_menu2()


def simulation():
    delta = 0
    return delta

def tick():
    c.after(400, tick)
    delta = simulation()
    global counter
    lbCounter['text'] = "Counter:\t\t" + str(counter)
    counter+=1

def start():
    global info
    info = Info(inputDoors.get(), inputGift.get(), inputRepetitions.get())
    visible_menu1()
    lbDoors['text']='Doors:\t\t'+str(info.doors)
    lbGift['text']='Gift:\t\t'+str(info.gift)
    lbRepetitions['text']='Repetitions:\t'+str(info.repetitions)
    c.after_idle(tick)


root = Tk()
root.title("Monte Carlo")
root.geometry("600x300+450+100")

lbDoors = Label(text="Doors")
lbGift = Label(text="Gifts")
lbRepetitions = Label(text="Repetitions")

lbCounter = Label(text="Counter")
left = Label(font='sans 10',text = '50 %',bg = 'green',height=2)
right = Label(font='sans 10',text = '50 %',bg  = 'red',height=2)

c = Canvas(root, width=1, height=1,bg  = 'white')

inputDoors = Entry()
inputGift = Entry()
inputRepetitions = Entry()

butStart = Button(root, height=1, width=10, text='Start', command=start)
butExit = Button(root, height=1, width=10, text='Exit', command=exit)

set_position_menu1()
root.mainloop()
