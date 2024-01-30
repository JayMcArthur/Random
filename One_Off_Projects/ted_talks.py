from tkinter import *
from random import randrange


def bonus_round():
    money = [0, 10, 1000, 1000, 10000]
    profit = 0
    while len(money) > 0:
        alt = []
        pick = randrange(0, len(money))
        for i in range(len(money)):
            if pick == i:
                if money[i] == 0:
                    return profit
                profit += money[i]
            else:
                alt.append(money[i])
        money = [*alt]


class Counter:
    def __init__(self):
        self.number = IntVar()
    def up(self):
        self.number.set(min(self.number.get()+1, 9))
    def down(self):
        self.number.set(max(self.number.get()-1, 0))
    def var(self):
        return self.number


class Display:
    def __init__(self):
        self.window = Tk()
        self.window.title("Counter")
        self.window.geometry('750x100')
        self.frame = Frame(self.window)
        self.frame.pack()
        self.counters = []

    def addCounter(self):
        new_counter = counter()

        frame_container = Entry(self.frame)
        frame_container.pack(side=LEFT)

        frame_display = Entry(frame_container)
        frame_display.pack(side=LEFT)

        the_pos = IntVar()
        the_pos.set(len(self.counters))

        pos = Entry(frame_display, text=the_pos, font="none 12", state=DISABLED, width=3)
        pos.pack(side=TOP)
        value = Entry(frame_display, textvariable=new_counter.var(), font="none 12", state=DISABLED, width=3)
        value.pack(side=BOTTOM)

        frame_buttons = Entry(frame_container)
        frame_buttons.pack(side=RIGHT)

        button_up = Button(frame_buttons, text="▲", font="none 10", command=new_counter.up)
        button_up.pack(side=TOP)
        button_down = Button(frame_buttons, text="▼", font="none 10", command=new_counter.down)
        button_down.pack(side=BOTTOM)

        self.counters.append(new_counter)

    def run(self):
        self.window.mainloop()


def da_vinci():
    # 1210
    # 3211000
    #

    main_display = display()
    for i in range(14):
        main_display.addCounter()
    main_display.run()