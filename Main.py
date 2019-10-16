import math
import random
from tkinter import *
from Info import Info
import time

info = Info
width_left_change_choise = 280
width_right_change_choise = 280
x_right_change_choise = 300
width_left_const_choise = 280
width_right_const_choise = 280
x_right_const_choise = 300
delta = 0
pause = 0
timer = 0
start_time = 0
finish_time = 0
number_winnings_change_choise = 0
number_winnings_const_choise = 0
counter_games = 0
fl_run = True
fl_start = False
fl_key = True
listDoors = []


def exit():
    root.destroy()


def set_position_menu2():
    lb_counter.place(x=240, y=70)
    but_exit.place(x=260, y=260)
    left.place(x=20, y=130, width=280)
    right.place(x=300, y=130, width=280)
    left2.place(x=20, y=170, width=280)
    right2.place(x=300, y=170, width=280)
    lb_doors.place(x=240, y=10)
    lb_gift.place(x=240, y=30)
    lb_repetitions.place(x=240, y=50)
    lb_time_simulation.place(x=240, y=90)


def set_position_menu1():
    input_doors.place(x=250, y=20)
    input_gift.place(x=250, y=40)
    input_repetitions.place(x=250, y=60)
    input_time_simulation.place(x=250, y=80)
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
    if counter_games <= getint(info.repetitions):
        lb_time_simulation['text'] = "Time (s):\t\t" + str(timer - start_time)


def simulation():
    initialize_game()
    my_choice = getint(random.randint(0, getint(info.doors) - 1))
    my_new_choice = my_choice

    while my_choice == my_new_choice:
        my_new_choice = getint(random.randint(0, getint(info.doors) - 1))

    if listDoors[my_new_choice] == 1:
        global number_winnings_change_choise
        number_winnings_change_choise += 1

    if listDoors[my_choice] == 1:
        global number_winnings_const_choise
        number_winnings_const_choise += 1

    global counter_games
    counter_games += 1


    global width_left_change_choise
    global delta
    width_left_change_choise = number_winnings_change_choise/counter_games*560
    left.place(width=width_left_change_choise)
    global x_right_change_choise
    delta = 560-width_left_change_choise
    x_right_change_choise = 580-delta
    global width_right_change_choise
    width_right_change_choise = delta
    right.place(x=x_right_change_choise, width=width_right_change_choise)

    global width_left_const_choise
    width_left_const_choise = number_winnings_const_choise / counter_games * 560
    left2.place(width=width_left_const_choise)
    global x_right_const_choise
    delta = 560 - width_left_const_choise
    x_right_const_choise = 580 - delta
    global width_right_const_choise
    width_right_const_choise = delta
    right2.place(x=x_right_const_choise, width=width_right_const_choise)

    left['text'] = str(math.ceil((width_left_change_choise/5.6)*100)/100)+" %"
    right['text'] = str(math.ceil((100-width_left_change_choise/5.6)*100)/100)+" %"
    left2['text'] = str(math.ceil((width_left_const_choise / 5.6) * 100) / 100) + " %"
    right2['text'] = str(math.ceil((100 - width_left_const_choise / 5.6) * 100) / 100) + " %"

    if counter_games >= getint(info.repetitions):
        global fl_run
        fl_run = False
        global finish_time
        finish_time = timer - start_time
        lb_time_simulation['text'] = "Time (s):\t\t" + str(finish_time)


def tick():
    if fl_run:
        global fl_start
        fl_start = True
        global pause
        pause = float(getint(info.time_simulation) / getint(info.repetitions))
        c.after(getint(pause * 1000), tick)
        simulation()
        lb_counter['text'] = "Counter:\t\t" + str(counter_games)


def initialize_game():
    global listDoors
    listDoors = [0 for x in range(getint(info.doors))]
    counter_number_gift = 0
    while counter_number_gift != getint(info.gift):
        index = random.randint(0, getint(info.doors) - 1)
        if listDoors[index] == 0:
            listDoors[index] = 1
            counter_number_gift += 1


def start():
    global info
    info = Info(input_doors.get(), input_gift.get(), input_repetitions.get(),
                input_time_simulation.get())
    initialize_game()
    visible_menu1()
    global delta
    delta = 560 / getdouble(info.repetitions)
    lb_doors['text'] = 'Doors:\t\t' + str(info.doors)
    lb_gift['text'] = 'Gift:\t\t' + str(info.gift)
    lb_repetitions['text'] = 'Repetitions:\t' + str(info.repetitions)
    c.after_idle(tick)


root = Tk()
root.title("Monte Carlo")
root.geometry("600x350+450+100")

lb_doors = Label(text="Doors")
lb_gift = Label(text="Gifts")
lb_repetitions = Label(text="Repetitions")
lb_time_simulation = Label(text="Time (s)")
lb_time_simulation.after_idle(clock)

lb_counter = Label(text="Counter")
left = Label(font='sans 10', text='50 %', bg='green', height=1)
right = Label(font='sans 10', text='50 %', bg='grey', height=1)
left2 = Label(font='sans 10', text='50 %', bg='red', height=1)
right2 = Label(font='sans 10', text='50 %', bg='grey', height=1)

c = Canvas(root, width=1, height=1, bg='white')

input_doors = Entry()
input_gift = Entry()
input_repetitions = Entry()
input_time_simulation = Entry()

but_start = Button(root, height=1, width=10, text='Start', command=start)
but_exit = Button(root, height=1, width=10, text='Exit', command=exit)

set_position_menu1()
root.mainloop()
