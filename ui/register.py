import tkinter as tk
from classes.user import user

class register_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Username:").pack(side=tk.TOP)
        username = tk.Entry(self).pack(side=tk.TOP)
        tk.Label(self, text="Password:").pack()
        password = tk.Entry(self).pack()
        tk.Label(self, text="Email:").pack()
        self.emailReg = tk.Entry(self)  # TODO add email validation
        self.emailReg.pack()
        tk.Button(self, text="Back", command=lambda: controller.show_frame("welcome_menu")).pack(side=tk.LEFT)
        tk.Button(self, text="Register", command=self.register).pack(side=tk.RIGHT)  # TODO add action register

        def register(self):
            if (user.isValidEmail(self.emailReg.get())):
                print("valid")
            else:
                tk.Label(self, text="Provided email is not valid", fg="red").pack()