import tkinter as tk
from tkinter import Entry, Label, Button

def calculate_inscribed_angles():
    try:
        inscribed_angle_1 = float(angle_entry.get())
        if 1 <= inscribed_angle_1 <= 179:
            inscribed_angle_2 = inscribed_angle_1
            result_label.config(text=f"The angle α is {inscribed_angle_1} degrees.\n"
                                     f"The angle β is also {inscribed_angle_2} degrees.\n"
                                     "Both angles are equal, as they are subtended by the same arc.",font=12)
        else:
            result_label.config(text="Please enter a valid angle measure between 0 and 179.",font=12)
    except ValueError:
        result_label.config(text="Please enter a valid number for the inscribed angle measure.",font=12)

# Create the main Tkinter window
root = tk.Tk()
root.geometry("500x400")
root.title("Inscribed Angles Calculator")


introlabel = Label(root, text="In circle O, arc AB subtends angle α  and angle β.",font=12)
introlabel.pack(pady=10,padx=10)
angle_label = Label(root, text="Enter the measure of the  inscribed angle α , (0-179 degrees):",font=12)
angle_label.pack(pady=10,padx=10)
#get user input
angle_entry = Entry(root)
angle_entry.pack(pady=10,padx=10)
#button
calculate_button = Button(root, font=12,text="Calculate", command=calculate_inscribed_angles)
calculate_button.pack(pady=10,padx=10)
#result shown after calculation
result_label = Label(root, text="")
result_label.pack(pady=10,padx=10)


root.mainloop()
