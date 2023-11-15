import tkinter as tk
from tkinter import Entry, Label, Button, Frame
from math import pi

def calculate_circle_area(radius, result_label):
    try:
        r = float(radius.get())
        if r > 0:
            area = 3.142 * r**2
            #:.2f means , cut off with 2 decimals
            result_label.config(text=f"The area of the circle is {area:.2f} square units.",font=12)
        else:
            result_label.config(text="Please enter a valid positive radius.",font=12)
    except ValueError:
        result_label.config(text="Please enter a valid number for the radius.",font=12)

def calculate_circle_volume(radius, result_label):
    try:
        r = float(radius.get())
        if r > 0:
            volume = (4/3) * 3.142 * r**3
            result_label.config(text=f"The volume of the circle is {volume:.2f} cubic units.",font=12)
        else:
            result_label.config(text="Please enter a valid positive radius.",font=12)
    except ValueError:
        result_label.config(text="Please enter a valid number for the radius.",font=12)

def display_circle_area(main_frame):
    clear_frame(main_frame)

    introlabel = Label(main_frame, text="Calculate the area of a circle.",font=12)
    introlabel.pack(pady=10, padx=10)

    radius_label = Label(main_frame, text="Enter the radius of the circle:",font=12)
    radius_label.pack(pady=10, padx=10)

    radius_entry = Entry(main_frame)
    radius_entry.pack(pady=10, padx=10)

    calculate_button = Button(main_frame,font=12, text="Calculate Area", command=lambda: calculate_circle_area(radius_entry, result_label))
    calculate_button.pack(pady=10, padx=10)

    result_label = Label(main_frame, text="")
    result_label.pack(pady=10, padx=10)

def display_circle_volume(main_frame):
    clear_frame(main_frame)

    introlabel = Label(main_frame, text="Calculate the volume of a circle.",font=12)
    introlabel.pack(pady=10, padx=10)

    radius_label = Label(main_frame, text="Enter the radius of the circle:",font=12)
    radius_label.pack(pady=10, padx=10)

    radius_entry = Entry(main_frame)
    radius_entry.pack(pady=10, padx=10)

    calculate_button = Button(main_frame, font=12,text="Calculate Volume", command=lambda: calculate_circle_volume(radius_entry, result_label))
    calculate_button.pack(pady=10, padx=10)

    result_label = Label(main_frame, text="")
    result_label.pack(pady=10, padx=10)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_circle_area():
    display_circle_area(main_frame)

def show_circle_volume():
    display_circle_volume(main_frame)

root = tk.Tk()
root.title("Circle area and volume Calculator")
root.geometry("652x512")

option_frame = Frame(root, bg='#c3c3c3')

circle_area_btn = Button(option_frame, text=' Circle Area ', font=('Bold', 15), command=show_circle_area)
circle_area_btn.place(x=10, y=50)

circle_volume_btn = Button(option_frame, text='Circle Volume', font=('Bold', 15), command=show_circle_volume)
circle_volume_btn.place(x=10, y=120)

option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=150, height=500)

main_frame = Frame(root, highlightbackground='grey', highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=500)

result_label = Label(main_frame, text="")
result_label.pack(padx=10, pady=10)

root.mainloop()
