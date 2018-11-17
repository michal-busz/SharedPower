import tkinter as tk
from classes.user import user

class login_menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        tk.Label(self, text="Username:").pack(side=tk.TOP)
        self.username = tk.Entry(self)
        self.username.pack(side=tk.TOP)
        tk.Label(self, text="Password:").pack()
        self.password = tk.Entry(self, show='*')
        self.password.pack()
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("welcome_menu")).pack(side=tk.LEFT)
        tk.Button(self, text="Login", command=self.login).pack(side=tk.RIGHT)  # TODO add action login
        self.invalidLogin = tk.Label(self,text="Invalid credentials. Please try again.",fg="red")

    def login(self):
        temp = user(self.username.get(), self.password.get())
        if(temp.auth()):
            self.controller.usr = temp
            self.controller.show_frame("logged_menu")
            self.controller.frames["logged_menu"].logged()
        else:
            self.invalidLogin.pack() #invalid login alert