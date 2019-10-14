from tkinter import *
from Info import Info
import time

info = Info
counter = 0
width_left = 280
width_right = 280
x_right = 300
delta = 0
pause = 0
timer = 0
start_time = 0
fl_run = True
fl_change_choice = True
fl_start = False


def exit():
    root.destroy()


def set_position_menu2():
    lb_counter.place(x=240, y=80)
    but_exit.place(x=260, y=250)
    left.place(x=20, y=130, width=280)
    right.place(x=300, y=130, width=280)
    lb_doors.place(x=240, y=20)
    lb_gift.place(x=240, y=40)
    lb_repetitions.place(x=240, y=60)
    lb_time_simulation.place(x=240, y=100)


def set_position_menu1():
    input_doors.place(x=250, y=20)
    input_gift.place(x=250, y=40)
    input_repetitions.place(x=250, y=60)
    input_time_simulation.place(x=250,y=80)
    lb_doors.place(x=180, y=20)
    lb_gift.place(x=180, y=40)
    lb_repetitions.place(x=180, y=60)
    lb_time_simulation.place(x=180, y=80)
    but_start.place(x=275, y=120)


def visible_menu2():
    if lb_counter.winfo_viewable():
        lb_counter.place_forget()
        but_exit.place_forget()
        right.place_forget()
        left.place_forget()
    else:
        set_position_menu2()


def visible_menu1():
    if lb_repetitions.winfo_viewable():
        input_doors.place_forget()
        input_repetitions.place_forget()
        input_gift.place_forget()
        but_start.place_forget()
        input_time_simulation.place_forget()
    else:
        set_position_menu1()
    visible_menu2()

def clock():
    lb_time_simulation.after(10, clock)
    global timer
    timer = time.perf_counter()
    global start_time
    timer = getint(timer)
    if not fl_start:
        timer = 0
        start_time = time.perf_counter()
        start_time = getint(start_time)
    lb_time_simulation['text'] = "Time (s):\t\t"+str(timer-start_time)

def simulation():
    global counter
    counter+=1
    if counter >= getint(info.repetitions):
        global fl_run
        fl_run = False


def tick():
    if fl_run:
        global fl_start
        fl_start = True
        global pause
        pause = float(getint(info.time_simulation)/getint(info.repetitions))
        c.after(getint(pause*1000), tick)
        simulation()
        global width_left
        global delta
        width_left += delta
        left.place(width=width_left)
        global x_right
        x_right += delta
        global width_right
        width_right -= delta
        right.place(x=x_right, width=width_right)
        lb_counter['text'] = "Counter:\t\t" + str(counter)



def start():
    global info
    info = Info(input_doors.get(), input_gift.get(), input_repetitions.get(),
                input_time_simulation.get())
    visible_menu1()
    global delta
    delta = 560 / getdouble(info.repetitions)
    lb_doors['text'] = 'Doors:\t\t' + str(info.doors)
    lb_gift['text'] = 'Gift:\t\t' + str(info.gift)
    lb_repetitions['text'] = 'Repetitions:\t' + str(info.repetitions)
    c.after_idle(tick)


root = Tk()
root.title("Monte Carlo")
root.geometry("600x300+450+100")

lb_doors = Label(text="Doors")
lb_gift = Label(text="Gifts")
lb_repetitions = Label(text="Repetitions")
lb_time_simulation = Label(text="Time (s)")
lb_time_simulation.after_idle(clock)

lb_counter = Label(text="Counter")
left = Label(font='sans 10', text='50 %', bg='green', height=2)
right = Label(font='sans 10', text='50 %', bg='red', height=2)

c = Canvas(root, width=1, height=1, bg='white')

input_doors = Entry()
input_gift = Entry()
input_repetitions = Entry()
input_time_simulation = Entry()

but_start = Button(root, height=1, width=10, text='Start', command=start)
but_exit = Button(root, height=1, width=10, text='Exit', command=exit)

set_position_menu1()
root.mainloop()
