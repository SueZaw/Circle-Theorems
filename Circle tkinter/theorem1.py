import tkinter as tk
from tkinter import Entry,Label,Button

def calculate_angles():

     try:
  
         inscribed_angle=float(entry_get.get())
         if 1 <= inscribed_angle <= 179:
        # Calculate the central angle
            central_angle= inscribed_angle * 2

            result.config(text=f"The central angle α is {central_angle} degrees.\n"
                               f"The inscribed angle β  is {inscribed_angle} degrees.", font=12)
         else:
            result.config(text="Please enter a valid central angle measure between 1 and 179.", font=12)
      
     except ValueError:
            result.config("Please enter a valid number for the central angle measure.", font=12)

root = tk.Tk()
root.title("Central angle and inscribed angle calculate")
root.geometry("500x300")

introlabel = Label(root, text="In circle O, arc AB subtends central angle α  and inscribed angle β.",font=12)
introlabel.pack(pady=10,padx=10)
angle_label = Label(root, text="Enter the measure of the  inscribed angle β, (1-179 degrees):",font=12)
angle_label.pack(pady=10,padx=10)
#get user input
entry_get=Entry(root)
entry_get.pack(padx=5,pady=5)
#calculate
button=Button(root,font=12,text="Calculate",command=calculate_angles)
button.pack(padx=5,pady=5)
#show the result
result=Label(root,text="")
result.pack(padx=10,pady=10)

root.mainloop()

