from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.pack()

#Buttons
def button_clicked():
    print(my_input.get())
    my_label.config(text=my_input.get())

button = Button(text="Update the Label!",command=button_clicked)
button.pack()

#Entries
my_input = Entry(width=40)
my_input.insert(END, string="Some text to begin with.")
my_input.pack()

#Text
text = Text(height=5, width=30)
text.focus()#Puts cursor in textbook
text.insert(END, "Example of multi-line text entry.")
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get()) #Prints 1 if On button checked, otherwise 0.

checked_state = IntVar() #Variable to hold on to checked state; 0 is off, 1 is on
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radiobutton_used():
    print(radiobutton_state.get())

radiobutton_state = IntVar() #Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radiobutton_state, command=radiobutton_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radiobutton_state, command=radiobutton_used)
radiobutton_state.get()
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) #Get current selection from listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()