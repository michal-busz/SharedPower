from tkinter import *

class menu:

    def __init__(self,master):
        self.master = master
        self.create_widgets()
    def test(self):
        print("test")

    def create_widgets(self):
        frame = Frame(self.master).pack()
        wLabel = Label(frame,text="Welcome! Shared Power v.0.1").pack()
        loginBt = Button(frame,text="Login",command=self.test()).pack()
        searchBt = Button(frame,text="Search for tools").pack()
        registerBt = Button(frame,text="Register an account").pack()
        quitBt = Button(frame, text="Exit",bg="red",command=self.master.destroy).pack()
        self.master.mainloop()
        #self.master.destroy() #required on Unix (Ubuntu) / executed after quit command
