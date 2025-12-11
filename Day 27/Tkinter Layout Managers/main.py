from tkinter import *
 
def button_clicked():
    print("The button is clicked!")

def change_label():
    my_label.config(text=my_input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Ariel", 24, "bold"))
my_label.config(text="New Text")
my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#Button    
button = Button(text="Update the Label!", command=change_label)
button.grid(column=1, row=1)

#New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()