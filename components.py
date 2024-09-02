from tkinter import *

#Setup Window
window=Tk()
window.geometry("300x300") #Setup Height & Width
window.config(bg="lightblue") #Window Background Color
window.title("My First GUI") #Set Title

#Components
#Button , Label , Text Input

#Label
My_Text = Label(text="Welcome to GUI Application")
My_Text.pack()

New_Text = Label(text="This is my Second Label")
New_Text.pack()

#Text Input
My_Box = Entry()
My_Box.pack()

#Button
# Submit = Button(text="Submit Now")
# Submit.pack()

#Button Function
#how to change label 

wish = Label(text="Hello")
wish.pack()


def WishMe():
    wish.config(text = f"Hello From {My_Box.get()}")


Hello = Button(text="Hello",command=WishMe) #No Bracket
Hello.pack()






window.mainloop()
