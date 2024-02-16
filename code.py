import tkinter
from tkinter import messagebox

def reset_entry():
    
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides',f'BMI = {bmi} is  Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides',f'BMI = {bmi} is Normal')
    else:
        messagebox.showinfo('bmi-pythonguides',f'BMI = {bmi} is  Overweight')
  
ws = tkinter.Tk()
ws.title('Body Mass Index Calculator')
ws.geometry('400x400')
label=tkinter.Label(ws,text="Body Mass Index Calculator")
label.pack()
var =tkinter.IntVar()

frame = tkinter.Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)

height_lb = tkinter.Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = tkinter.Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = tkinter.Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = tkinter.Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

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
cal_btn = tkinter.Button(
    frame31,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack()

reset_btn = tkinter.Button(
    frame32,
    text='Reset',
    command=reset_entry
)
reset_btn.pack()
exit_btn = tkinter.Button(
    frame33,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack()

ws.mainloop()
