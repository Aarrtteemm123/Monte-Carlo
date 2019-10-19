import math
import random
from tkinter import *
from Info import Info
import time

class Application(object):

    def __init__(self,root):
        self.info = Info(3, 1, 1000, 10)
        self.width_left_change_choise = 280
        self.width_right_change_choise = 280
        self.x_right_change_choise = 300
        self.width_left_const_choise = 280
        self.width_right_const_choise = 280
        self.x_right_const_choise = 300
        self.delta = 0
        self.pause = 0
        self.timer = 0
        self.start_time = 0
        self.finish_time = 0
        self.number_winnings_change_choise = 0
        self.number_winnings_const_choise = 0
        self.index_door_host = 0
        self.counter_games = 0
        self.fl_run = True
        self.fl_start = False
        self.fl_key = True
        self.listDoors = []
        self.root = root
        self.lb_doors = Label(text="Doors")
        self.lb_gift = Label(text="Gifts")
        self.lb_repetitions = Label(text="Repetitions")
        self.lb_time_simulation = Label(text="Time (s)")
        self.lb_info_red = Label(text=" ", bg='orangered')
        self.lb_info_red_text = Label(text="- change choice", font='sans 10')
        self.lb_info_green = Label(text=" ", bg='limegreen')
        self.lb_info_green_text = Label(text="- not change choice", font='sans 10')
        self.lb_info_gray = Label(text=" ", bg='#8c8c8c')
        self.lb_info_gray_text = Label(text="- losing", font='sans 10')
        self.lb_delta = Label(font='sans 10')
        self.lb_time_simulation.after_idle(self.clock)

        self.lb_counter = Label(text="Counter")
        self.left = Label(font='sans 10', text='50 %', bg='limegreen', height=1)
        self.right = Label(font='sans 10', text='50 %', bg='#8c8c8c', height=1)
        self.left2 = Label(font='sans 10', text='50 %', bg='orangered', height=1)
        self.right2 = Label(font='sans 10', text='50 %', bg='#8c8c8c', height=1)

        self.c = Canvas(root, width=1, height=1, bg='white')

        self.input_doors = Entry()
        self.input_gift = Entry()
        self.input_repetitions = Entry()
        self.input_time_simulation = Entry()

        self.but_start = Button(root, height=1, width=10, text='Start', command=self.start)
        self.but_exit = Button(root, height=1, width=10, text='Back', command=self.back_to_menu)

    def reset(self):
        self.fl_run = True
        self.fl_start = False
        self.fl_key = True
        self.counter_games = 0
        self.pause = 0
        self.timer = 0
        self.start_time = 0
        self.finish_time = 0
        self.number_winnings_change_choise = 0
        self.number_winnings_const_choise = 0


    def back_to_menu(self):
        self.fl_run = False
        self.visible_menu1()
        self.input_doors.delete(first=0, last=END)
        self.input_gift.delete(first=0, last=END)
        self.input_repetitions.delete(first=0, last=END)
        self.input_time_simulation.delete(first=0, last=END)
        self.input_doors.insert(index=0, string=self.info.doors)
        self.input_gift.insert(index=0, string=self.info.gift)
        self.input_repetitions.insert(index=0, string=self.info.repetitions)
        self.input_time_simulation.insert(index=0, string=self.info.time_simulation)


    def set_position_menu2(self):
        self.lb_counter.place(x=240, y=70)
        self.but_exit.place(x=260, y=290)
        self.left.place(x=20, y=130, width=280)
        self.right.place(x=300, y=130, width=280)
        self.left2.place(x=20, y=170, width=280)
        self.right2.place(x=300, y=170, width=280)
        self.lb_doors.place(x=240, y=10)
        self.lb_gift.place(x=240, y=30)
        self.lb_repetitions.place(x=240, y=50)
        self.lb_time_simulation.place(x=240, y=90)
        self.lb_delta.place(x=260,y=205)

        k=100
        self.lb_info_green.place(x=20+k, y=240,width=20,height=20)
        self.lb_info_green_text.place(x=45+k, y=240)
        self.lb_info_red.place(x=180+k, y=240,width=20,height=20)
        self.lb_info_red_text.place(x=205+k, y=240)
        self.lb_info_gray.place(x=320+k, y=240,width=20,height=20)
        self.lb_info_gray_text.place(x=345+k, y=240)


    def set_position_menu1(self):
        self.input_doors.place(x=250, y=20)
        self.input_gift.place(x=250, y=40)
        self.input_repetitions.place(x=250, y=60)
        self.input_time_simulation.place(x=250, y=80)
        self.lb_doors.place(x=180, y=20)
        self.lb_gift.place(x=180, y=40)
        self.lb_repetitions.place(x=180, y=60)
        self.lb_time_simulation.place(x=180, y=80)
        self.but_start.place(x=275, y=120)


    def visible_menu2(self):
        if self.lb_counter.winfo_viewable():
            self.lb_counter.place_forget()
            self.but_exit.place_forget()
            self.right.place_forget()
            self.left.place_forget()
            self.right2.place_forget()
            self.left2.place_forget()
            self.lb_info_green.place_forget()
            self.lb_info_green_text.place_forget()
            self.lb_info_red.place_forget()
            self.lb_info_red_text.place_forget()
            self.lb_info_gray.place_forget()
            self.lb_info_gray_text.place_forget()
            self.lb_delta.place_forget()
            self.set_position_menu1()
        else:
            self.set_position_menu2()


    def visible_menu1(self):
        if self.lb_repetitions.winfo_viewable():
            self.input_doors.place_forget()
            self.input_repetitions.place_forget()
            self.input_gift.place_forget()
            self.but_start.place_forget()
            self.input_time_simulation.place_forget()
            self.visible_menu2()
        else:
            self.set_position_menu1()


    def clock(self):
        self.timer = time.monotonic()
        self.lb_time_simulation['text'] = "Time (s):\t\t" + str(getint(self.timer - self.start_time))


    def simulation(self):
        self.initialize_game()
        my_choice = getint(random.randint(0, getint(self.info.doors) - 1))
        index_door_host = my_new_choice = my_choice

        while index_door_host == my_choice or self.listDoors[index_door_host] == 1:
            index_door_host = getint(random.randint(0, getint(self.info.doors) - 1))

        while my_choice == my_new_choice or my_new_choice == index_door_host:
            my_new_choice = getint(random.randint(0, getint(self.info.doors) - 1))

        if self.listDoors[my_new_choice] == 1:
            self.number_winnings_change_choise += 1

        if self.listDoors[my_choice] == 1:
            self.number_winnings_const_choise += 1

        self.counter_games += 1

        width_left_change_choise = self.number_winnings_change_choise / self.counter_games * 560
        self.left.place(width=width_left_change_choise)
        self.delta = 560 - width_left_change_choise
        x_right_change_choise = 580 - self.delta
        width_right_change_choise = self.delta
        self.right.place(x=x_right_change_choise, width=width_right_change_choise)

        width_left_const_choise = self.number_winnings_const_choise / self.counter_games * 560
        self.left2.place(width=width_left_const_choise)
        self.delta = 560 - width_left_const_choise
        x_right_const_choise = 580 - self.delta
        width_right_const_choise = self.delta
        self.right2.place(x=x_right_const_choise, width=width_right_const_choise)

        self.left['text'] = str(math.ceil((width_left_change_choise / 5.6) * 100) / 100) + " %"
        self.right['text'] = str(math.ceil((100 - width_left_change_choise / 5.6) * 100) / 100) + " %"
        self.left2['text'] = str(math.ceil((width_left_const_choise / 5.6) * 100) / 100) + " %"
        self.right2['text'] = str(math.ceil((100 - width_left_const_choise / 5.6) * 100) / 100) + " %"
        difference = (math.ceil((width_left_change_choise / 5.6) * 100) / 100)-(math.ceil((width_left_const_choise / 5.6) * 100) / 100)
        self.lb_delta['text'] ="Delta = "+str(math.ceil(difference*100)/100)+" %"
        if self.counter_games >= getint(self.info.repetitions):
            self.fl_run = False


    def tick(self):
        if self.fl_run:
            self.fl_start = True
            pause = float(getint(self.info.time_simulation) / getint(self.info.repetitions))
            self.c.after(getint(pause * 1000), self.tick)
            self.simulation()
            self.lb_time_simulation.after_idle(self.clock)
            self.lb_counter['text'] = "Counter:\t\t" + str(self.counter_games)


    def initialize_game(self):
        self.info = Info(3, 1, 1000, 10)
        self.listDoors = [0 for x in range(getint(self.info.doors))]
        counter_number_gift = 0
        while counter_number_gift != getint(self.info.gift):
            index = random.randint(0, getint(self.info.doors) - 1)
            if self.listDoors[index] == 0:
                self.listDoors[index] = 1
                counter_number_gift += 1


    def start(self):
        self.reset()
        self.info = Info(self.input_doors.get(), self.input_gift.get(), self.input_repetitions.get(),
                    self.input_time_simulation.get())
        self.initialize_game()
        self.visible_menu1()
        self.delta = 560 / getdouble(self.info.repetitions)
        self.lb_doors['text'] = 'Doors:\t\t' + str(self.info.doors)
        self.lb_gift['text'] = 'Gift:\t\t' + str(self.info.gift)
        self.lb_repetitions['text'] = 'Repetitions:\t' + str(self.info.repetitions)
        self.start_time = time.monotonic()
        self.c.after_idle(self.tick)

    def app_run(self):
        self.back_to_menu()
        self.set_position_menu1()
        self.root.mainloop()