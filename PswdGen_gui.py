from tkinter import *

from random import randint
def generate():
    password.delete(0, END)
    length=int(charanswer.get())
    pswd = ''
    for x in range(length):
        pswd += chr(randint(33, 126))
    password.insert(0, pswd)
    
window = Tk()

window.title("Password Generator")
window.geometry('600x500')

nameframe = LabelFrame(window, text = "Enter Username : ", font = "timesnewroman 15")
nameframe.pack(padx=10,pady=40)

nameanswer = Entry(nameframe, width = 30, font = "timesnewroman 15")
nameanswer.pack(padx=5,pady=15)

charframe = LabelFrame(window, text = "Number Of Characters:", font = "timesnewroman 15")
charframe.pack(padx=10, pady=20)

charanswer = Entry(charframe, width = 10, font = "timesnewroman 15")
charanswer.pack(padx=5, pady=10)

Buttonframe = Frame(window)
Buttonframe.pack(pady = 20)

enerateBtn = Button(Buttonframe, text = "Generate", font = "lucida 20", command = generate)
enerateBtn.grid(row=0, column=2)

password = Entry(window, text='', font = "lucida 20")
password.pack()

window.mainloop()