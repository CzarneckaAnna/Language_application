"""The mail goal of this project is to create application, which will monitoring language progress.
   At the beginning application will have only timer, calendar and flash cards."""
import tkinter

MAIN_COLOR = "#caf7e3"


# TODO 2: Working with clock (start, stop, refresh - think about pomodoro clock option.
def start():
    pass


def stop():
    pass


# TODO 3: Working with calendar (for now create only Mon-Sun. option)
def calendar():
    pass


def statistic():
    pass


# TODO 4: Working with flash cards (start button, import flash card words, save progress).
def cards():
    pass


# TODO 1: Create desktop with clock, week-calendar and flash card button.
window = tkinter.Tk()
window.title("Language progress")
window.config(padx=100, pady=50, width=500, height=224,  bg=MAIN_COLOR)

timer = tkinter.Label(text="0:00")
timer.grid(column=0, row=0)

check = tkinter.Label(text="1:00")
check.grid(column=1, row=0)

text = tkinter.Label(text="4:00")
text.grid(column=0, row=1, columnspan=2, rowspan=2)

start_button = tkinter.Button(command=start, highlightthickness=0)
start_button.config(text="START")
start_button.grid(column=2, row=0)

stop_button = tkinter.Button(command=stop, highlightthickness=0)
stop_button.config(text="STOP")
stop_button.grid(column=2, row=1)

flash_card = tkinter.Button(command=cards, highlightthickness=0)
flash_card.config(text="Flash Cards")
flash_card.grid(column=2, row=2)

stat = tkinter.Button(command=statistic, highlightthickness=0)
stat.config(text="Statistics")
stat.grid(column=2, row=3)

week_stat = tkinter.Label(text="aaa")
week_stat.grid(column=0, row=3, columnspan=2)



window.mainloop()
