from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Date:").grid(row=1, column=0, padx=10, pady=10)
date_entry = Entry(root)
date_entry.grid(row=1, column=1)

Label(root, text="Month:").grid(row=2, column=0, padx=10, pady=10)
month_entry = Entry(root)
month_entry.grid(row=2, column=1)

Label(root, text="Year:").grid(row=3, column=0, padx=10, pady=10)
year_entry = Entry(root)
year_entry.grid(row=3, column=1)

result_label = Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=20)

def calculate_age():
    name = name_entry.get()
    d = int(date_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())

    today = date.today()
    age = today.year - y

    if (today.month, today.day) < (m, d):
        age -= 1

    result_label.config(text=f"Hello {name}! Your age is {age} years.")

Button(root, text="Calculate Age", command=calculate_age).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
