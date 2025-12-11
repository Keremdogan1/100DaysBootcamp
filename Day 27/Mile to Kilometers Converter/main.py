WIDTH = 10
HEIGHT = 2
MULTIPLY = 1.60934 

from tkinter import *

def calculate():
    miles = float(entry.get())
    kilometers = miles * MULTIPLY
    converted_label.config(text=int(kilometers))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(pady=40)

entry = Entry(width=WIDTH)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Ariel", 12, "normal"), width=WIDTH, height=HEIGHT)
miles_label.grid(column=2,row=0)

is_equal_to_label = Label(text="is equal to", font=("Ariel", 12, "normal"), width=WIDTH, height=HEIGHT)
is_equal_to_label.grid(column=0, row=1)

converted_label = Label(text=0, font=("Ariel", 12, "normal"), width=WIDTH, height=HEIGHT)
converted_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Ariel", 12, "normal"), width=WIDTH, height=HEIGHT)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()