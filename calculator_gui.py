from tkinter import *
def click(event) : 
    global scvalue
    text = event.widget.cget("text")
    print(text)
    
    if text == "=" : 
        if scvalue.get().isdigit() : 
            value = int(scvalue.get())
    
        else : 
            
            try : 
                value = eval(screen.get())
            except Exception as e :
                print(e)
                value = "Error"
                
        scvalue.set(value)
        screen.update()

        print(value)


    elif text == "C" :
        scvalue.set("")
        screen.update()
    
    
    else : 
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("544x750")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font = "lucida 40 bold")
screen.pack(fill = X, ipadx = 8, pady = 10, padx = 10) 

#Make frames with 3 buttons each
a = Frame(root, bg = "grey")

b = Button(a, text = "9",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 10)
b.bind("<Button-1>", click)

b = Button(a, text = "8",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 10)
b.bind("<Button-1>", click)

b = Button(a, text = "7",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 10)
b.bind("<Button-1>", click)

a.pack()


a = Frame(root, bg = "grey")
b = Button(a, text = "6",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 10)
b.bind("<Button-1>", click)

b = Button(a, text = "5",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 10)
b.bind("<Button-1>", click)

b = Button(a, text = "4",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 10)
b.bind("<Button-1>", click)

a.pack()


a = Frame(root, bg = "grey")
b = Button(a, text = "3",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 5)
b.bind("<Button-1>", click)

b = Button(a, text = "2",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 5)
b.bind("<Button-1>", click)

b = Button(a, text = "1",padx = 15, pady = 10, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 10, pady = 5)
b.bind("<Button-1>", click)

a.pack()

a = Frame(root, bg = "grey")

b = Button(a, text = "0",padx = 15, pady = 15, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 11, pady = 4)
b.bind("<Button-1>", click)

b = Button(a, text = "-",padx = 15, pady = 10, font = "lucida 28 bold")
b.pack(side = LEFT, padx = 11, pady = 3)
b.bind("<Button-1>", click)

b = Button(a, text = "*",padx = 15, pady = 15, font = "lucida 25 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

a.pack()

a = Frame(root, bg = "grey")

b = Button(a, text = "/",padx = 12, pady = 10, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 12, pady = 5)
b.bind("<Button-1>", click)

b = Button(a, text = "%",padx = 13, pady = 18, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(a, text = "=",padx = 12, pady = 15, font = "lucida 26 bold")
b.pack(side = LEFT, padx = 14, pady = 5)
b.bind("<Button-1>", click)

a.pack()

a = Frame(root, bg = "grey")
b = Button(a, text = "C",padx = 19, pady = 15, font = "lucida 22 bold")
b.pack(side = LEFT, padx = 9, pady = 5)
b.bind("<Button-1>", click)

b = Button(a, text = "+",padx = 17, pady = 12, font = "lucida 26 bold")
b.pack(side = LEFT, padx = 9, pady = 5)
b.bind("<Button-1>", click)

b = Button(a, text = "00",padx = 12, pady = 15, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 9, pady = 5)
b.bind("<Button-1>", click)

a.pack()

root.mainloop()