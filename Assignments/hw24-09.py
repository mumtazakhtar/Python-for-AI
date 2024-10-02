from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("oops implementation")

guielements = ["Label","Button","Dropdown"]

dropdown = ttk.Combobox(root,state="readyonly",values=guielements)
dropdown.pack()

class CreateElements:
    def __init__(self):
        print("This is create element class")
        
    def createlabel(self):
        label=Label(root, text="new label is created using oops", fg="blue")
        label.pack()
        
    def createbutton(self):
        classbtn=Button(root, text="button")
        classbtn.pack(padx=20, pady=10)
    
    def createDropdown(self):
        value=[1,2,3,4]
        classdropdown = ttk.Combobox(root, state="readonly", values=value)
        classdropdown.pack()
        
    def choose(self):
        global dropdown
        element=dropdown.get()
        if(element == "Label"):
           self.createlabel()
        elif(element == "Button"):
           self.createbutton()
        elif(element == "Dropdown"):
            self.createDropdown()
        
object1 = CreateElements()
btn = Button(root, text="create element", command= object1.choose)
btn.pack(padx=20, pady=10)

root.mainloop()
         
         
        