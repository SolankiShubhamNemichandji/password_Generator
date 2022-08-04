from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passletters=[choice(letters) for i in range(randint(8,10))]
    passsymbols=[choice(symbols) for i in range(randint(2,4))]
    passnumbers=[choice(numbers) for i in range(randint(2,4))]
    passwdlist=passletters+passsymbols+passnumbers
    shuffle(passwdlist)
    gen_passwd="".join(passwdlist)
    passwdentry.insert(0, gen_passwd)
    pyperclip.copy(gen_passwd)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web=webentry.get()
    email=mailentry.get()
    passwd=passwdentry.get()
    newdata={
                web:{
                    "email":email,
                    "password":passwd
                }
    }
    if len(web)==0 or len(passwd)==0:
        messagebox.showinfo(title="Oops", message="Don't left any fields empty.")
    else:
        try:
            with open("savedata.json", "r") as data:
                d=json.load(data)
        except FileNotFoundError:
            with open("savedata.json", "w") as data:
                json.dump(newdata, data, indent=4)
        else:
            d.update(newdata)
            with open("savedata.json", "w") as data:
                json.dump(d, data, indent=4)
        finally:
            webentry.delete(0, END)
            passwdentry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search_data():

    with open("savedata.json","r") as data:
        d=json.load(data)
        website=webentry.get()
        passw=d[website]["password"]
        messagebox.showinfo(title="Your Data", message=f"Website:{website}\nPassword:{passw}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=40, bg="black")
heading=Label(text="Your Password Generator", fg="red", bg="black", font=("Courier", 20, "bold"))
heading.grid(column=1, row=0, columnspan=2)
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=img)
canvas.grid(column=1, row=1, columnspan=2)

l1 = Label(text="Website", bg="black", fg="white")
l1.grid(column=0, row=2)

l2 = Label(text="Email", bg="black", fg="white")
l2.grid(column=0, row=3)

l3 = Label(text="Password", bg="black", fg="white")
l3.grid(column=0, row=4)

webentry=Entry(width=30, bg="black", fg="white", insertbackground="red")
webentry.grid(column=1, row=2)
webentry.focus()
search=Button(text="Search", width=23, command=search_data, bg="black", fg="white")
search.grid(column=2, row=2)

mailentry=Entry(width=60, bg="black", fg="white")
mailentry.grid(column=1, row=3, columnspan=2)
mailentry.insert(0, "shubhams2909@gmail.com")

passwdentry=Entry(width=31, bg="black", fg="white", insertbackground="red")
passwdentry.grid(column=1, row=4)
passwdentry.focus()

generate = Button(text="Generate", width=22, command=generate, bg="black", fg="white")
generate.grid(column=2, row=4)

add = Button(text="Add", width=22, command=save, bg="black", fg="white")
add.grid(column=1, row=5)

window.mainloop()