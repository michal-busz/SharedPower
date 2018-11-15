from tkinter import *
from classes.user import user
import re

class menu:

    def __init__(self,master):
        self.master = master
        self.frame= Frame()
        self.frameInit()
        self.welcome_menu()

    def frameInit(self):
        self.frame.destroy()
        self.frame = Frame(self.master)
        self.frame.pack()

    def welcome_menu(self):
        self.frameInit()
        Label(self.frame,text="Welcome! Shared Power v.0.1").pack() #welcome message
        Button(self.frame,text="Login",command=self.login_menu).pack()
        Button(self.frame,text="Search for tools").pack()
        Button(self.frame,text="Register an account", command=self.register_menu).pack()
        Button(self.frame, text="Exit",bg="red",command=self.master.destroy).pack()
        #self.master.destroy() #required on Unix (Ubuntu) (?) not sure

    def login_menu(self):
        self.frameInit()
        Label(self.frame,text="Username:").pack(side=TOP)
        username = Entry(self.frame).pack(side = TOP)
        Label(self.frame,text="Password:").pack()
        password = Entry(self.frame, show='*').pack()
        Button(self.frame,text="Back",command=self.welcome_menu).pack(side = LEFT)
        Button(self.frame, text="Login").pack(side=RIGHT)  # TODO add action login

    def register_menu(self):
        self.frameInit()
        Label(self.frame, text="Username:").pack(side=TOP)
        username = Entry(self.frame).pack(side=TOP)
        Label(self.frame, text="Password:").pack()
        password = Entry(self.frame).pack()
        Label(self.frame, text="Email:").pack()
        self.emailReg = Entry(self.frame) #TODO add email validation
        self.emailReg.pack()
        Button(self.frame, text="Back", command=self.welcome_menu).pack(side=LEFT)
        Button(self.frame, text="Register", command=self.register).pack(side=RIGHT) #TODO add action register

    def register(self):
        if(user.isValidEmail(self.emailReg.get())):
            print("valid")
        else:
            Label(self.frame,text="Provided email is not valid",fg="red").pack()



