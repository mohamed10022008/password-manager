from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_email():
    w = website_entry.get()
    e = Email_and_username_entry.get()
    p = Password_entry.get()

    if len(w) == 0 or len(p) == 0 or len(e) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=w, message="these are the details entered : " + w + "\n" + e + "\n" + p)

        if is_ok:
            with open("my_password.txt", mode="a") as my_pass:
                my_pass.write(w + " " + '|' + " " + e + " " + '|' + " " + p + "\n")
            website_entry.delete(0, END)
            Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(pady=50, padx=50)

# Labels

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

Email_and_username_label = Label(text="Email/Username")
Email_and_username_label.grid(row=2, column=0)

Password_label = Label(text="Password")
Password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

Email_and_username_entry = Entry(width=40)
Email_and_username_entry.grid(column=1, row=2, columnspan=2)
Email_and_username_entry.insert(0, "marchmellomohamed@gmail.com")

Password_entry = Entry(width=25)
Password_entry.grid(column=1, row=3, columnspan=2)

# Buttons

Password_button = Button(width=5, text="G.P", command=new_password)
Password_button.grid(column=2, row=3, columnspan=3)

Add_Button = Button(width=36, text="Add", command=add_email)
Add_Button.grid(column=1, row=4, columnspan=2)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

window.mainloop()
