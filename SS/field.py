import tkinter as tk
from tkinter import messagebox
import pyperclip

# read data from data.txt
with open("data.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# index to track which line
current_index = 0

def show_field():
    if 0 <= current_index < len(lines):
        field_text.set(lines[current_index])
        pyperclip.copy(lines[current_index])
    else:
        messagebox.showinfo("Done", "✅ All fields reviewed!")

def next_field():
    global current_index
    current_index += 1
    show_field()

def previous_field():
    global current_index
    current_index -= 1
    show_field()

# create GUI
root = tk.Tk()
root.title("Field Checker")

field_text = tk.StringVar()
field_text.set(lines[current_index])

label = tk.Label(root, textvariable=field_text, font=("Courier", 14), wraplength=600, justify="left")
label.pack(padx=20, pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

prev_btn = tk.Button(button_frame, text="Previous", command=previous_field)
prev_btn.pack(side=tk.LEFT, padx=10)

next_btn = tk.Button(button_frame, text="Next", command=next_field)
next_btn.pack(side=tk.LEFT, padx=10)

instructions = tk.Label(root, text="Copied to clipboard automatically. Press Ctrl+F in browser to search.", fg="green")
instructions.pack(pady=10)

root.mainloop()
