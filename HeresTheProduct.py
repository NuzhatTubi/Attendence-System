from tkinter import *

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Result: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

root = Tk()
root.title("Multiply Two Numbers")

label1 = Label(root, text="Enter the first number:")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter the second number:")
label2.pack()

entry2 = Entry(root)
entry2.pack()

calc_button = Button(root, text="Calculate", command=calculate_product)
calc_button.pack()

result_label = Label(root, text="Result:")
result_label.pack()

root.mainloop()
