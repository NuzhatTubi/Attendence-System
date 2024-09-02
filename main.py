from tkinter import *

window=Tk()
window.config(bg="lightblue")
window.title("Smart Attendence Portal")
window.geometry("500x500")

header=Label(text="Smart Attendence System For Class Seven",bg="lightblue",fg="navyblue",font=("TimesNewRoman",15,"bold"))
header.pack()

def mark_attendance(name):
    print(f"{name} Present .")

def show_student():
    for names in studslist:
       mybutton=Button(text=names,bg="cyan",fg="blue",font=("Ariel",10,"bold"),padx=10,pady=7,relief="raised",bd=5,command=lambda name=names: mark_attendance(name))
       mybutton.pack()




students=Button(text="Click To View",bg="lightgreen",fg="darkgreen",font=("ComicSans",10,"italic","bold"),padx=15,pady=10,relief="raised",bd=3,command=show_student)
students.pack()

studslist=["Rayeed Raj","Nuzhat Tubi","Emma Frost","Anonti Ahmed","Zaara Larson","James McAvoy","William Shakesphere","Henry Cavill"]

window.mainloop()