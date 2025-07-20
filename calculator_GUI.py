import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
from tkinter import messagebox
first_number=second_number=operator=None

def get_digit(digit):
    current_text = result_label['text']
    new_text = current_text + str(digit)
    result_label.config(text=new_text)
def clear_result():
    result_label.config(text="")
def calculate_result(op):
    global first_number,operator
    
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text="")
def get_result():
    global first_number, second_number, operator
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text= str(first_number - second_number))
    elif operator == '*':
        result_label.config(text= str(first_number * second_number))
    else:
        if second_number == '0':
            result_label.config(text= 'Error')
        else:
            result_label.config(text= str(first_number / second_number))
root = tk.Tk()
root.title("Calculator GUI")
root.geometry("220x290")
root.resizable(False, False)
root.configure(bg="#353A38")
result_label = tk.Label(root, text="", bg="#353A38", fg="#FFFFFF")
result_label.grid(row=0, column=0,columnspan=10, pady=(20,25),sticky="e")
result_label.config(font=("Arial", 24))


button7 = tk.Button(root, text="7", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(7))
button7.grid(row=1, column=0, padx=5, pady=5)


button8 = tk.Button(root, text="8", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(8))
button8.grid(row=1, column=1, padx=5, pady=5)


button9 = tk.Button(root, text="9", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(9))
button9.grid(row=1, column=2, padx=5, pady=5)


button4 = tk.Button(root, text="4", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(4))  
button4.grid(row=2, column=0, padx=5, pady=5)


button5 = tk.Button(root, text="5", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(5))
button5.grid(row=2, column=1, padx=5, pady=5) 

      
button6 = tk.Button(root, text="6", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(6))
button6.grid(row=2, column=2, padx=5, pady=5)


button1 = tk.Button(root, text="1", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(1))
button1.grid(row=3, column=0, padx=5, pady=5)


button2 = tk.Button(root, text="2", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(2))  
button2.grid(row=3, column=1, padx=5, pady=5)


button3 = tk.Button(root, text="3", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(3))
button3.grid(row=3, column=2, padx=5, pady=5)


button0 = tk.Button(root, text="0", width=5, height=2, bg="#4A4E4D", fg="#FFFFFF",command= lambda: get_digit(0))
button0.grid(row=4, column=0, padx=5, pady=5)


button_clear = tk.Button(root, text="C", width=5, height=2, bg="#FF6347", fg="#FFFFFF",command= lambda: clear_result())
button_clear.grid(row=4, column=1, padx=5, pady=5)


button_equals = tk.Button(root, text="=", width=5, height=2, bg="#4A90E2", fg="#FFFFFF",command= lambda: get_result())
button_equals.grid(row=4, column=2, padx=5, pady=5)


button_add = tk.Button(root, text="+", width=5, height=2, bg="#4A90E2", fg="#FFFFFF",command=lambda: calculate_result('+'))
button_add.grid(row=1, column=4, padx=5, pady=5)


button_subtract = tk.Button(root, text="-", width=5, height=2, bg="#4A90E2", fg="#FFFFFF",command=lambda: calculate_result('-'))
button_subtract.grid(row=2, column=4, padx=5, pady=5)


button_multiply = tk.Button(root, text="*", width=5, height=2, bg="#4A90E2", fg="#FFFFFF",command=lambda: calculate_result('*'))
button_multiply.grid(row=3, column=4, padx=5, pady=5)


button_divide = tk.Button(root, text="/", width=5, height=2, bg="#4A90E2", fg="#FFFFFF",command=lambda: calculate_result('/'))
button_divide.grid(row=4, column=4, padx=5, pady=5)



root.mainloop()
