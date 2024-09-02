from tkinter import *

window=Tk()
window.title("Age Calculator")
window.geometry("250x150")
window.config(bg="lightblue")

#labels

header=Label(text="Welcome to tha Age Calculator application.")
header.pack()

ttitle=Label(text="Enter your birth year.")
ttitle.pack()

#text

my_text=Entry()
my_text.pack()
 
def my_age():
    current_year=2024
    year =my_text.get()
    age=current_year-int(year)
    your_age.config(text=age)


button=Button(text="Your Age",command=my_age)
button.pack()

your_age=Label()
your_age.pack()



window.mainloop()