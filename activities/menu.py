from tkinter import *

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
        #TODO consider removing unused variables below
        wLabel = Label(self.frame,text="Welcome! Shared Power v.0.1").pack()
        loginBt = Button(self.frame,text="Login",command=self.login_menu).pack()
        searchBt = Button(self.frame,text="Search for tools").pack()
        registerBt = Button(self.frame,text="Register an account", command=self.register_menu).pack()
        quitBt = Button(self.frame, text="Exit",bg="red",command=self.master.destroy).pack()
        #self.master.destroy() #required on Unix (Ubuntu) (?) not sure

    def login_menu(self):
        self.frameInit()
        unLbl = Label(self.frame,text="Username:").pack(side=TOP)
        username = Entry(self.frame).pack(side = TOP)
        pwLbl = Label(self.frame,text="Password:").pack()
        password = Entry(self.frame, show='*').pack()
        backBt = Button(self.frame,text="Back",command=self.welcome_menu).pack(side = BOTTOM)

    def register_menu(self):
        self.frameInit()
        unLbl = Label(self.frame, text="Username:").pack(side=TOP)
        username = Entry(self.frame).pack(side=TOP)
        pwLbl = Label(self.frame, text="Password:").pack()
        password = Entry(self.frame, show='*').pack()
        emLbl = Label(self.frame, text="Email:").pack()
        email = Entry(self.frame).pack() #TODO add email validation
        backBt = Button(self.frame, text="Back", command=self.welcome_menu).pack(side=LEFT)
        registerBt = Button(self.frame, text="Register").pack(side=RIGHT) #TODO add action register
