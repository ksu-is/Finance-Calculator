#Finance Calculator by Rachel Straiton
#User will be prompted with questions to figure out the NPV of a project
#When user answers questions, their input will be appended to a list that will store their information
#This information will be used by the calculator to calculate the NPV
#Then the program will make a decision ('yes' or 'no) as response to user
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        

        
    def init_window(self):
        self.master.title("NPV Calc")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit",menu=edit)
    
    def client_exit(self):
        exit()
    

root = Tk()
root.geometry("400x300")

text = Text(root, width="10",height="1")
#text.pack()

text1 = Text(root, width="10",height="1")
#text1.pack()

label_1 = Label(root, width="20",height="3",bg="red",text="Intial Outlay")
label_2 = Label(root,width="20",height="3",bg="blue",text="Operating Cash Flow")

button_1=Button(root,text="Click me")

label_1.grid(row=0,column=0)
label_2.grid(row=1,column=0)

button_1.grid(row=2,column=2)

text.grid(row=0, column=2)
text1.grid(row=1, column=2)

#app = Window(root)
root.mainloop()
