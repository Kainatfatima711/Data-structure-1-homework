import tkinter as tk

window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

def convert():
    inches = entry.get()
    if inches.isdigit():
        cm = float(inches) * 2.54
        result_label.config(text="Centimeters: " + str(round(cm, 2)))
    else:
        result_label.config(text="Please enter a number")

title_label = tk.Label(window, text="Length Converter", font=("Arial", 16))
title_label.pack(pady=20)

input_label = tk.Label(window, text="Enter length in inches:")
input_label.pack()

entry = tk.Entry(window)
entry.pack(pady=10)

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="Centimeters: ")
result_label.pack(pady=20)

window.mainloop()
