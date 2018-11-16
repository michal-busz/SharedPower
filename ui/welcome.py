import tkinter as tk

class welcome_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #TODO commands below objects
        tk.Label(self, text="Welcome! Shared Power v.0.1").pack()  # welcome message
        tk.Button(self, text="Login", command=lambda: controller.show_frame("login_menu")).pack()
        tk.Button(self, text="Search for tools").pack()
        tk.Button(self, text="Register an account", command=lambda: controller.show_frame("register_menu")).pack()
        tk.Button(self, text="Exit", bg="red", command=controller.destroy).pack()
        # self.master.destroy() #required on Unix (Ubuntu) (?) not sure