import math
import random
from tkinter import *
from Info import Info
import time


class Application(object):

    def __init__(self, root):
        self.__info = Info(3, 1, 1000, 10)
        self.__width_left_change_choise = 280
        self.__width_right_change_choise = 280
        self.__x_right_change_choise = 300
        self.__width_left_const_choise = 280
        self.__width_right_const_choise = 280
        self.__x_right_const_choise = 300
        self.__delta = 0
        self.__pause = 0
        self.__timer = 0
        self.__start_time = 0
        self.__finish_time = 0
        self.__number_winnings_change_choise = 0
        self.__number_winnings_const_choise = 0
        self.__index_door_host = 0
        self.__counter_games = 0
        self.__fl_run = True
        self.__fl_start = False
        self.__fl_key = True
        self.__listDoors = []
        self.__root = root
        self.__lb_doors = Label(text="Doors")
        self.__lb_gift = Label(text="Gifts")
        self.__lb_repetitions = Label(text="Repetitions")
        self.__lb_time_simulation = Label(text="Time (s)")
        self.__lb_info_red = Label(text=" ", bg='orangered')
        self.__lb_info_red_text = Label(text="- change choice", font='sans 10')
        self.__lb_info_green = Label(text=" ", bg='limegreen')
        self.__lb_info_green_text = Label(text="- not change choice", font='sans 10')
        self.__lb_info_gray = Label(text=" ", bg='#8c8c8c')
        self.__lb_info_gray_text = Label(text="- losing", font='sans 10')
        self.__lb_delta = Label(font='sans 10')
        self.__lb_time_simulation.after_idle(self.__clock)

        self.__lb_counter = Label(text="Counter")
        self.__left = Label(font='sans 10', text='50 %', bg='limegreen', height=1)
        self.__right = Label(font='sans 10', text='50 %', bg='#8c8c8c', height=1)
        self.__left2 = Label(font='sans 10', text='50 %', bg='orangered', height=1)
        self.__right2 = Label(font='sans 10', text='50 %', bg='#8c8c8c', height=1)

        self.__c = Canvas(root, width=1, height=1, bg='white')

        self.__input_doors = Entry()
        self.__input_gift = Entry()
        self.__input_repetitions = Entry()
        self.__input_time_simulation = Entry()

        self.__but_start = Button(root, height=1, width=10, text='Start', command=self.__start)
        self.__but_exit = Button(root, height=1, width=10, text='Back', command=self.__back_to_menu)

    def __reset(self):
        self.__fl_run = True
        self.__fl_start = False
        self.__fl_key = True
        self.__counter_games = 0
        self.__pause = 0
        self.__timer = 0
        self.__start_time = 0
        self.__finish_time = 0
        self.__number_winnings_change_choise = 0
        self.__number_winnings_const_choise = 0

    def __back_to_menu(self):
        self.__fl_run = False
        self.__visible_menu1()
        self.__input_doors.delete(first=0, last=END)
        self.__input_gift.delete(first=0, last=END)
        self.__input_repetitions.delete(first=0, last=END)
        self.__input_time_simulation.delete(first=0, last=END)
        self.__input_doors.insert(index=0, string=self.__info.doors)
        self.__input_gift.insert(index=0, string=self.__info.gift)
        self.__input_repetitions.insert(index=0, string=self.__info.repetitions)
        self.__input_time_simulation.insert(index=0, string=self.__info.time_simulation)

    def __set_position_menu2(self):
        self.__lb_counter.place(x=240, y=70)
        self.__but_exit.place(x=260, y=290)
        self.__left.place(x=20, y=130, width=280)
        self.__right.place(x=300, y=130, width=280)
        self.__left2.place(x=20, y=170, width=280)
        self.__right2.place(x=300, y=170, width=280)
        self.__lb_doors.place(x=240, y=10)
        self.__lb_gift.place(x=240, y=30)
        self.__lb_repetitions.place(x=240, y=50)
        self.__lb_time_simulation.place(x=240, y=90)
        self.__lb_delta.place(x=260, y=205)

        k = 100
        self.__lb_info_green.place(x=20 + k, y=240, width=20, height=20)
        self.__lb_info_green_text.place(x=45 + k, y=240)
        self.__lb_info_red.place(x=180 + k, y=240, width=20, height=20)
        self.__lb_info_red_text.place(x=205 + k, y=240)
        self.__lb_info_gray.place(x=320 + k, y=240, width=20, height=20)
        self.__lb_info_gray_text.place(x=345 + k, y=240)

    def __set_position_menu1(self):
        self.__input_doors.place(x=250, y=20)
        self.__input_gift.place(x=250, y=40)
        self.__input_repetitions.place(x=250, y=60)
        self.__input_time_simulation.place(x=250, y=80)
        self.__lb_doors.place(x=180, y=20)
        self.__lb_gift.place(x=180, y=40)
        self.__lb_repetitions.place(x=180, y=60)
        self.__lb_time_simulation.place(x=180, y=80)
        self.__but_start.place(x=275, y=120)

    def __visible_menu2(self):
        if self.__lb_counter.winfo_viewable():
            self.__lb_counter.place_forget()
            self.__but_exit.place_forget()
            self.__right.place_forget()
            self.__left.place_forget()
            self.__right2.place_forget()
            self.__left2.place_forget()
            self.__lb_info_green.place_forget()
            self.__lb_info_green_text.place_forget()
            self.__lb_info_red.place_forget()
            self.__lb_info_red_text.place_forget()
            self.__lb_info_gray.place_forget()
            self.__lb_info_gray_text.place_forget()
            self.__lb_delta.place_forget()
            self.__set_position_menu1()
        else:
            self.__set_position_menu2()

    def __visible_menu1(self):
        if self.__lb_repetitions.winfo_viewable():
            self.__input_doors.place_forget()
            self.__input_repetitions.place_forget()
            self.__input_gift.place_forget()
            self.__but_start.place_forget()
            self.__input_time_simulation.place_forget()
            self.__visible_menu2()
        else:
            self.__set_position_menu1()

    def __clock(self):
        self.__timer = time.monotonic()
        self.__lb_time_simulation['text'] = "Time (s):\t\t" + str(getint(self.__timer - self.__start_time))

    def __simulation(self):
        self.__initialize_game()
        my_choice = getint(random.randint(0, getint(self.__info.doors) - 1))
        index_door_host = my_new_choice = my_choice

        while index_door_host == my_choice or self.__listDoors[index_door_host] == 1:
            index_door_host = getint(random.randint(0, getint(self.__info.doors) - 1))

        while my_choice == my_new_choice or my_new_choice == index_door_host:
            my_new_choice = getint(random.randint(0, getint(self.__info.doors) - 1))

        if self.__listDoors[my_new_choice] == 1:
            self.__number_winnings_change_choise += 1

        if self.__listDoors[my_choice] == 1:
            self.__number_winnings_const_choise += 1

        self.__counter_games += 1

        width_left_change_choise = self.__number_winnings_change_choise / self.__counter_games * 560
        self.__left.place(width=width_left_change_choise)
        self.__delta = 560 - width_left_change_choise
        x_right_change_choise = 580 - self.__delta
        width_right_change_choise = self.__delta
        self.__right.place(x=x_right_change_choise, width=width_right_change_choise)

        width_left_const_choise = self.__number_winnings_const_choise / self.__counter_games * 560
        self.__left2.place(width=width_left_const_choise)
        self.__delta = 560 - width_left_const_choise
        x_right_const_choise = 580 - self.__delta
        width_right_const_choise = self.__delta
        self.__right2.place(x=x_right_const_choise, width=width_right_const_choise)

        self.__left['text'] = str(math.ceil((width_left_change_choise / 5.6) * 100) / 100) + " %"
        self.__right['text'] = str(math.ceil((100 - width_left_change_choise / 5.6) * 100) / 100) + " %"
        self.__left2['text'] = str(math.ceil((width_left_const_choise / 5.6) * 100) / 100) + " %"
        self.__right2['text'] = str(math.ceil((100 - width_left_const_choise / 5.6) * 100) / 100) + " %"
        difference = (math.ceil((width_left_change_choise / 5.6) * 100) / 100) - (
                    math.ceil((width_left_const_choise / 5.6) * 100) / 100)
        self.__lb_delta['text'] = "Delta = " + str(math.ceil(difference * 100) / 100) + " %"
        if self.__counter_games >= getint(self.__info.repetitions):
            self.__fl_run = False

    def __tick(self):
        if self.__fl_run:
            self.__fl_start = True
            pause = float(getint(self.__info.time_simulation) / getint(self.__info.repetitions))
            self.__c.after(getint(pause * 1000), self.__tick)
            self.__simulation()
            self.__lb_time_simulation.after_idle(self.__clock)
            self.__lb_counter['text'] = "Counter:\t\t" + str(self.__counter_games)

    def __initialize_game(self):
        self.__listDoors = [0 for x in range(getint(self.__info.doors))]
        counter_number_gift = 0
        while counter_number_gift != getint(self.__info.gift):
            index = random.randint(0, getint(self.__info.doors) - 1)
            if self.__listDoors[index] == 0:
                self.__listDoors[index] = 1
                counter_number_gift += 1

    def __check_data(self):
        if getint(self.__info.doors) <= 0 or getint(self.__info.gift) <= 0:
            self.__info = Info(3, 1, 1000, 10)
        if getint(self.__info.doors) - getint(self.__info.gift) < 2:
            self.__info.gift = getint(self.__info.doors) - 2

    def __start(self):
        self.__reset()
        self.__info = Info(self.__input_doors.get(), self.__input_gift.get(), self.__input_repetitions.get(),
                           self.__input_time_simulation.get())
        self.__check_data()
        self.__initialize_game()
        self.__visible_menu1()
        self.__delta = 560 / getdouble(self.__info.repetitions)
        self.__lb_doors['text'] = 'Doors:\t\t' + str(self.__info.doors)
        self.__lb_gift['text'] = 'Gift:\t\t' + str(self.__info.gift)
        self.__lb_repetitions['text'] = 'Repetitions:\t' + str(self.__info.repetitions)
        self.__start_time = time.monotonic()
        self.__c.after_idle(self.__tick)

    def app_run(self):
        self.__back_to_menu()
        self.__set_position_menu1()
        self.__root.mainloop()
