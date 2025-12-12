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
CHECK_MARK = "✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    top_label.config(text="Timer", bg=YELLOW, fg=GREEN)
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 2 == 1 and reps < 8:
        top_label.config(text="Work", bg=YELLOW, fg=GREEN)
        countdown(work_seconds)
    elif reps == 8:
        top_label.config(text="Break", bg=YELLOW, fg=PINK)
        check_mark_label.config(text=CHECK_MARK * (reps // 2))
        countdown(long_break_seconds)
    elif reps < 8:
        top_label.config(text="Break", bg=YELLOW, fg=RED)
        check_mark_label.config(text=CHECK_MARK * (reps // 2))
        countdown(short_break_seconds)
    else:
        top_label.config(text="Timer", bg=YELLOW, fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(total_seconds):
    global reps
    global timer

    mins = str(math.floor(total_seconds/60))
    seconds = total_seconds % 60

    if total_seconds > 0:
        if seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)

        timer = window.after(1000, countdown, total_seconds - 1)
    else:
        mins = "0"
        seconds = "00"

        if reps <= 8:
            start_timer()
    
    canvas_time = f"{mins}:{seconds}"
    canvas.itemconfig(timer_text, text=canvas_time)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

top_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"),bg=YELLOW , fg=GREEN)
top_label.grid(column=1, row=0)

check_mark_label = Label(font=(FONT_NAME, 20, "bold") ,bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)

window.mainloop()

