import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I Am a Label", font=("Ariel", 24, "bold"))
my_label.pack(side="top", expand=True)

window.mainloop()

import turtle

tim = turtle.Turtle()
tim.write("Some Text")