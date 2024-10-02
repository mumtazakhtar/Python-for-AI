from tkinter import *
root = Tk()
root.geometry("700x700")
root.title("oops implementation")

class CreateElements:
    def __init__(self):
        print("create element class")
    def createNewElements(self):
        label = Label(root, text="a new label created using class")
        label.pack()# this will create below each other other than using axis
        classbtn = Button(root, text = "Button is created")
        classbtn.pack()
        
obj = CreateElements()
btn = Button(root, text="click to create label and button" ,command=obj.createNewElements)
btn.pack()

root.mainloop()