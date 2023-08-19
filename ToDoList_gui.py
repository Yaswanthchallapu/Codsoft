from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        list.insert(ANCHOR, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    list.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')

ws.title('TO-DO LIST')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

list = Listbox(
    frame,
    width=27,
    height=9,
    font=('Times', 19),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",   
)
list.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    list.insert(END, item)

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=BOTH)

list.config(yscrollcommand=scroll.set)
scroll.config(command=list.yview)

my_entry = Entry(
    ws,
    font=('times', 26)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='ADD TASK',
    font=('times 16'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='DELETE TASK',
    font=('times 16'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()