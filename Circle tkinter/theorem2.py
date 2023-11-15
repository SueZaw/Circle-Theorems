import tkinter as tk
from tkinter import Label,Entry,Button
def calculate_cyclic_quadrilateral_angles():   
    try:
         angle_A=float(entry_get1.get())
         angle_B=float(entry_get2.get())

         if 1 <= angle_A <= 179 and 1 <= angle_B <= 179:
        # Set angles C and D 
           angle_C = 180-angle_A
           angle_D = 180-angle_B

           result.config(text=f"The measure of angle A is {angle_A} degrees.\n"
                               f"The measure of angle B is {angle_B} degrees.\n"
                               f"The measure of angle C is also {angle_C} degrees.\n"
                               f"The measure of angle D is also {angle_D} degrees.",font=12)
         else:
            result.config(text="Please enter valid angle measures between 1 and 179.",font=12)
    except ValueError:
         result.config(text="Please enter valid numbers for the angle measures.",font=12)


root=tk.Tk() 
root.geometry("500x400")
root.title("Cyclic quadrilateral calculate")

introlabel = Label(root, text="In circle O,  ABCD is cyclic quardrilateral.",font=12)
introlabel.pack(pady=10,padx=10)

angle_label1= Label(root, text="Enter the measure of angle A , (1-179 degrees):",font=12)
angle_label1.pack(pady=10,padx=10)
#getting the user input
entry_get1=Entry(root)
entry_get1.pack(padx=10,pady=10)

angle_label2= Label(root, text="Enter the measure of angle B , (1-179 degrees):",font=12)
angle_label2.pack(pady=10,padx=10)
#getting the user input
entry_get2=Entry(root)
entry_get2.pack(padx=10,pady=10)

#calculate 
button=Button(root,text="Calculate",command=calculate_cyclic_quadrilateral_angles,font=12)
button.pack(padx=5,pady=5)

#show result
result=Label(root,text="")
result.pack(padx=10,pady=10)

root.mainloop()