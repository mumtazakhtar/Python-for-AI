# password generator 

from tkinter import *
import random

root = Tk()
root.title("password generator")
root.geometry("400x400")

label = Label(root)
array_3d = [[['1','2','3','4','5','6'],["head","tail"],["A","B","C","D","E","F"]]]

def newpassword():
    random1 = random.randint(0,5)
    random2 = random.randint(0,1)
    random3 = random.randint(0,4)
    
    letter1 = array_3d[0][0][random1]
    letter2 = array_3d[0][1][random2]
    letter3 = array_3d[0][2][random3]
    
    label["text"] = letter1+letter2+letter3
    
btn = Button(root, text="Generate Password", command=newpassword)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5,rely=0.6, anchor=CENTER)
    
root.mainloop()