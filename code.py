import tkinter
from tkinter import messagebox

#Method to reset data
def reset():
    
    height.delete(0,'end')
    weight.delete(0,'end')
    

#Method compute BMI
def calculate():
    kilograms = int(weight.get())
    mass = int(height.get())/100
    bmi = kilograms/(mass*mass)
    bmi = round(bmi, 1)
    index(bmi)


#Method classify BMI
def index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides',f'BMI = {bmi} is  Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides',f'BMI = {bmi} is Normal')
    else:
        messagebox.showinfo('bmi-pythonguides',f'BMI = {bmi} is  Overweight')
#Defining window and naming.  
window = tkinter.Tk()
window.title('Body Mass Index Calculator')
window.geometry('400x400')
label=tkinter.Label(window,text="Body Mass Index Calculator")
label.pack()
var =tkinter.IntVar()

#Adding dimensions to frame.
frame = tkinter.Frame(
    window,
    padx=10, 
    pady=10
)
frame.pack(expand=True)

#Tab for height
height_lb = tkinter.Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

#Tab for weight
weight_lb = tkinter.Label(
    frame,
    text="Enter Weight (in kilograms)  ",

)
weight_lb.grid(row=4, column=1)

#Height input
height = tkinter.Entry(
    frame,
)
height.grid(row=3, column=2, pady=5)

#Weight input
weight = tkinter.Entry(
    frame,
)
weight.grid(row=4, column=2, pady=5)


#Defing frames for calculate, reset and exit options
frame31 = tkinter.Frame(
    frame
)
frame32 = tkinter.Frame(
    frame
)
frame33 = tkinter.Frame(
    frame
)
frame31.grid(row=5, columnspan=3, pady=10)
frame32.grid(row=6, columnspan=3, pady=10)
frame33.grid(row=7, columnspan=3, pady=10)

#Calcutate
cal_btn = tkinter.Button(
    frame31,
    text='Calculate',
    command=calculate
)
cal_btn.pack()

#Reset
reset_btn = tkinter.Button(
    frame32,
    text='Reset',
    command=reset
)
reset_btn.pack()

#Exit
exit_btn = tkinter.Button(
    frame33,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack()

#Diplays window until terminated by user.
ws.mainloop()
