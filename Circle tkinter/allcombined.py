import tkinter as tk
from tkinter import Entry, Label, Button, Frame

def display_corollary1(main_frame):
    clear_frame(main_frame)

    introlabel = Label(main_frame,font=12, text="In circle O, arc AB subtends angle α and angle β.")
    introlabel.pack(pady=10, padx=10)

    angle_label = Label(main_frame, font=12,text="Enter the measure of the inscribed angle α (0-179 degrees):")
    angle_label.pack(pady=10, padx=10)

    angle_entry = Entry(main_frame)
    angle_entry.pack(pady=10, padx=10)

    calculate_button = Button(main_frame, font=12,text="Calculate", command=lambda: calculate_inscribed_angles(angle_entry, result_label))
    calculate_button.pack(pady=10, padx=10)

    result_label = Label(main_frame, text="")
    result_label.pack(pady=10, padx=10)

def display_theorem1(main_frame):
    clear_frame(main_frame)

    introlabel = Label(main_frame, font=12,text="In circle O, arc AB subtends central angle α and inscribed angle β.")
    introlabel.pack(pady=10, padx=10)

    angle_label = Label(main_frame, font=12,text="Enter the measure of the inscribed angle β, (1-179 degrees):")
    angle_label.pack(pady=10, padx=10)

    entry_get = Entry(main_frame)
    entry_get.pack(padx=5, pady=5)

    button = Button(main_frame, font=12,text="Calculate", command=lambda: calculate_angles(entry_get, result_label))
    button.pack(padx=5, pady=5)

    result_label = Label(main_frame, text="")
    result_label.pack(padx=10, pady=10)

def display_theorem2(main_frame):
    clear_frame(main_frame)

    introlabel = Label(main_frame, font=12,text="In circle O, ABCD is a cyclic quadrilateral.")
    introlabel.pack(pady=10, padx=10)

    angle_label1 = Label(main_frame, font=12,text="Enter the measure of angle A , (1-179 degrees):")
    angle_label1.pack(pady=10, padx=10)

    entry_get1 = Entry(main_frame)
    entry_get1.pack(padx=10, pady=10)

    angle_label2 = Label(main_frame, font=12,text="Enter the measure of angle B , (1-179 degrees):")
    angle_label2.pack(pady=10, padx=10)

    entry_get2 = Entry(main_frame)
    entry_get2.pack(padx=10, pady=10)

    button = Button(main_frame,font=12, text="Calculate", command=lambda: calculate_cyclic_quadrilateral_angles(entry_get1, entry_get2, result_label))
    button.pack(padx=5, pady=5)

    result_label = Label(main_frame, text="")
    result_label.pack(padx=10, pady=10)

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

#Calculation functions
 #corollary1.1
def calculate_inscribed_angles(angle_entry, result_label):
    try:
        inscribed_angle_1 = float(angle_entry.get())
        if 1 <= inscribed_angle_1 <= 179:
            result_label.config(text=f"The angle α is {inscribed_angle_1} degrees.\n"
                                     f"The angle β is also {inscribed_angle_1} degrees.\n"
                                     "Both angles are equal, as they are subtended by the same arc.",font=12)
        else:
            result_label.config(text="Please enter a valid angle measure between 0 and 179.",font=12)
    except ValueError:
        result_label.config(text="Please enter a valid number for the inscribed angle measure.",font=12)

#theorem1
def calculate_angles(entry_get, result_label):
    try:
        inscribed_angle = float(entry_get.get())
        if 1 <= inscribed_angle <= 179:
            # Calculate the central angle
            central_angle = inscribed_angle * 2

            result_label.config(text=f"The central angle α is {central_angle} degrees.\n"
                               f"The inscribed angle β  is {inscribed_angle} degrees.", font=12)
        else:
            result_label.config(text="Please enter a valid central angle measure between 1 and 179.",font=12)
    except ValueError:
        result_label.config(text="Please enter a valid number for the central angle measure.",font=12)

#theorem2
def calculate_cyclic_quadrilateral_angles(entry_get1, entry_get2, result_label):
    try:
        angle_A = float(entry_get1.get())
        angle_B = float(entry_get2.get())

        if 1 <= angle_A <= 179 and 1 <= angle_B <= 179:
            # Set angles C and D
            angle_C = 180 - angle_A
            angle_D = 180 - angle_B

            result_label.config(text=f"The measure of angle A is {angle_A} degrees.\n"
                               f"The measure of angle B is {angle_B} degrees.\n"
                               f"The measure of angle C is also {angle_C} degrees.\n"
                               f"The measure of angle D is also {angle_D} degrees.",font=12)
        else:
            result_label.config(text="Please enter valid angle measures between 1 and 179.",font=12)
    except ValueError:
        result_label.config(text="Please enter valid numbers for the angle measures.",font=12)

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

#clearing frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#showing 
def show_corollary1():
    display_corollary1(main_frame)

def show_theorem1():
    display_theorem1(main_frame)

def show_theorem2():
    display_theorem2(main_frame)

def show_circle_area():
    display_circle_area(main_frame)

def show_circle_volume():
    display_circle_volume(main_frame)

root = tk.Tk()
root.title("Circle Calculator")
root.geometry("657x506")

option_frame = Frame(root, bg='#c3c3c3')

corollary1_btn = Button(option_frame, text=' Corollary1.1', font=('Bold', 15), command=show_corollary1)
corollary1_btn.place(x=10, y=50)

theorem1_btn = Button(option_frame, text='  Theorem1  ', font=('Bold', 15), command=show_theorem1)
theorem1_btn.place(x=10, y=120) 

theorem2_btn = Button(option_frame, text='  Theorem2  ', font=('Bold', 15), command=show_theorem2)
theorem2_btn.place(x=10, y=190)

circle_area_btn = Button(option_frame, text=' Circle Area  ', font=('Bold', 15), command=show_circle_area)
circle_area_btn.place(x=10, y=260)

circle_volume_btn = Button(option_frame, text='Circle Volume', font=('Bold', 15), command=show_circle_volume)
circle_volume_btn.place(x=10, y=330)

option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=155, height=500)

main_frame = Frame(root, highlightbackground='grey', highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=500)

result_label = Label(main_frame, text="")
result_label.pack(padx=10, pady=10)

root.mainloop()
