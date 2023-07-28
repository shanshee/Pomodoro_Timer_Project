from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checks = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    check_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text='Study', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = round(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global checks
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            checks += '✔'
        check_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 27, 'bold'))
canvas.grid(column=1, row=1)

# labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text='', font=(FONT_NAME, 15, 'bold'), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# buttons
start_button = Button(text='Start', width=4, font=('Calibri', 10, 'normal'), bg=PINK, fg='white', command=start_timer)
start_button.config(padx=5, pady=10)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', width=4, font=('Calibri', 10, 'normal'), bg=PINK, fg='white', command=reset_timer)
reset_button.config(padx=5, pady=10)
reset_button.grid(column=2, row=2)

window.mainloop()
