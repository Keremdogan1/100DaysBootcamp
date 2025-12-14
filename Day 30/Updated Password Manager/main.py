from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "": 
        messagebox.showwarning(title="Failure", message="Please don't leave any spaces empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password} \n\nIs it OK to save?")

        if is_ok:
            try:
                with open("passwords.json", "r") as passwords:
                    try:
                        data = json.load(passwords)
                    except:
                        data = new_data

            except FileNotFoundError:
                with open("passwords.json", "w") as passwords:
                    json.dump(new_data, passwords, indent=4)
            else:
                try:
                    check_same_website = {wanted_website:key for (wanted_website,key) in data.items() if wanted_website == website}
                except:
                    check_same_website = ""

                if check_same_website == "":
                    data.update(new_data)

                    with open("passwords.json", "w") as passwords:
                        json.dump(data, passwords, indent=4)
                else:
                    if messagebox.askokcancel(title="Warning", message=f"You have data for {website}, do you want to overwrite?"):
                        data[website]["email"] = email
                        data[website]["password"] = password

                        with open("passwords.json", "w") as passwords:
                            json.dump(data, passwords, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            messagebox.showinfo(title="Success", message="Details are saved succesfully.")

# ---------------------------- WEBSITE SEARCH ------------------------------- #
def search_website():
    website = website_entry.get()

    if website != "":
        try:
            with open("passwords.json", "r") as passwords:
                try:
                    data = json.load(passwords)
                    try:
                        website_to_search = {wanted_website:key for (wanted_website,key) in data.items() if wanted_website == website}
                    except:
                        messagebox.showwarning(title="Failure", message=f"There is no saved data for {website}.")
                    else:
                        messagebox.showinfo(title=website, message=f"Email: {website_to_search[website]["email"]} \nPassword: {website_to_search[website]["password"]}")
                except:
                    messagebox.showwarning(title="Failure", message=f"There is no data in file.")
        except:
            messagebox.showwarning(title="Failure", message=f"Data file does not exists.")
    else:
        messagebox.showwarning(title="Failure", message="Please don't leave website space empty!")

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

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

website_search_button = Button(text="Search", command=search_website, width=14)
website_search_button.grid(row=1, column=2) 

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