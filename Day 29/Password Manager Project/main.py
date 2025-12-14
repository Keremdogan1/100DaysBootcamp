from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    
    password_list.append([random.choice(letters) for _ in range(nr_letters)])
    password_list.append([random.choice(numbers) for _ in range(nr_numbers)])
    password_list.append([random.choice(symbols) for _ in range(nr_symbols)])
    
    password_list = [x for sublist in password_list for x in sublist]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    formatted_website = f"{website:<20}"
    formatted_email = f"{email:<25}"

    if website == "" or email == "" or password == "": 
        messagebox.showwarning(title="Failure", message="Please don't leave any spaces empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password} \n\nIs it OK to save?")

        if is_ok:
            with open("passwords.txt", "a") as passwords:
                passwords.write(f"{formatted_website} | {formatted_email} | {password} \n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title="Success", message="Details are saved succesfully.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Ariel", 12, "normal"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:", font=("Ariel", 12, "normal"))
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=52)
email_username_entry.insert(0, "kerem.dogan111@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=("Ariel", 12, "normal"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()