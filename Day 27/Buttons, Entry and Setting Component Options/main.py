from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I Am a Label", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

#Button

def button_clicked():
    my_label.config(text=my_input.get())
    

button = Button(text="Update the Label!",command=button_clicked)
button.pack()

#Entry

my_input = Entry(width=10)

my_input.pack()


window.mainloop()