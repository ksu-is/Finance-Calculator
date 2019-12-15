#Finance Calculator by Rachel Straiton
#User will be prompted with questions to figure out the NPV of a project
#When user answers questions, their input will be appended to a list that will store their information
#This information will be used by the calculator to calculate the NPV
#Then the program will make a decision ('yes' or 'no) as response to user
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()
        self.create_widget()

    def init_window(self):
        self.master.title("NPV Calculator")
        #self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Learn More",command=self.about_me)
        menu.add_cascade(label="About",menu=edit)

    def clear_widget(self,widget,widgets):
        widget.destroy()    
        widgets.destroy()
        
    def about_me(self):
        self.about = Label(self, width="50",height="5",bg="#52EB7B", text="This is Rachel's Corporate Finance Calculator\n that makes it easy to solve for NPV!",font=("Courier New",12))
        self.about.grid(row=10,column=0,columnspan=6)
        self.about_btn = Button(self, width="5",height="1",text="X",command=lambda: self.clear_widget(self.about,self.about_btn))
        self.about_btn.grid(row=9,column=5)

    def client_exit(self):
        exit()
        
    def calculate(self):
        self.answer.delete(0,END)
        initialOutlay = self.text_1.get("1.0",END)
        ocf = self.text_2.get("1.0",END)
        tv = self.text_3.get("1.0",END)
        n = self.text_4.get("1.0",END)
        r = self.text_5.get("1.0",END)

        ocf_1 = 1 + float(r)
        ocf_2 = float(ocf_1) ** float(n)
        ocf_3 = 1 / float(ocf_2)
        ocf_4 = 1 - float(ocf_3)
        ocf_5 = float(ocf_4) / float(r)
        ocf_answer = float(ocf) * float(ocf_5)

        tv_1 = 1 + float(r)
        tv_2 = float(tv_1) ** float(n)
        tv_3 = 1 / float(tv_2)
        tv_answer = float(tv) * float(tv_3)

        final_answer = float(initialOutlay) + float(ocf_answer) + float(tv_answer)
        if final_answer >= 0:
            self.yes = Label(self,width="20",height="3",bg="green",text="Yes, take the project.")
            self.yes.grid(row=5,column=2,columnspan=2)
        else:
            self.no = Label(self,width="20",height="3",bg="red",text="No, do not take the project.")
            self.no.grid(row=5,column=2,columnspan=2)
        self.answer.insert("0", final_answer)
        return
        
    #NPV = IO + OCF x {[1-(1/(1+r)^n)]/r} + TV x [1/(1+r)^n]

    def create_widget(self):
        self.text_1 = Text(self, width="20",height="1")
        self.text_1.grid(row=0, column=2)

        self.text_2 = Text(self, width="20",height="1")
        self.text_2.grid(row=1, column=2)

        self.text_3 = Text(self, width="20",height="1")
        self.text_3.grid(row=2, column=2)

        self.text_4 = Text(self, width="20",height="1")
        self.text_4.grid(row=0,column=5)

        self.text_5 = Text(self, width="20",height="1")
        self.text_5.grid(row=1,column=5)

        self.io = Label(self, width="20",height="3",bg="#900C3F",text="Intial Outlay")
        self.io.grid(row=0,column=0)

        self.ocf = Label(self,width="20",height="3",bg="#C70039",text="Operating Cash Flow")
        self.ocf.grid(row=1,column=0)

        self.tv = Label(self,width="20",height="3",bg="#FF5733",text="Terminal Value")
        self.tv.grid(row=2,column=0)

        self.project = Label(self, width="20",height="3",bg="#FFC300",text="Length of Project")
        self.project.grid(row=0,column=3)

        self.r = Label(self, width="20",height="3",bg="#DAF7A6",text="Discount Rate (r)")
        self.r.grid(row=1,column=3)

        self.button_1=Button(self,bg="#B5CFD8",text="Net Present Value $",command=self.calculate)
        self.button_1.grid(row=2,column=3,columnspan=2)

        self.answer = Entry(root,text="",font=("Courier New",25))
        self.answer.grid(row=9,column=0)



root = Tk()
root.geometry("600x400")
root.resizable(0,0)
app = Application(root)
root.mainloop()

