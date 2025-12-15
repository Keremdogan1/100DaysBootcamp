from tkinter import *
import pandas
import random

current_card = ""
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- READ DATA ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

# ---------------------------- SELECT RANDOM WORD ------------------------------- #
def select_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=show_english)

def show_english():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# ---------------------------- SAVE PROGRESS ------------------------------- #
def update_csv():
    global current_card
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=show_english)

french_or_english = "french"
face_of_canvas = "front"
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=select_word)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=lambda:[select_word(), update_csv()])
right_button.grid(column=1, row=1)

select_word()

window.mainloop()