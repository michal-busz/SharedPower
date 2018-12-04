import tkinter as tk

class welcome_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()

        tk.Label(self, text="Welcome! Shared Power v.0.1").grid()  # welcome message
        tk.Button(self, text="Login", command=lambda: controller.show_frame("login_menu")).grid()
        tk.Button(self, text="Search for tools").grid()
        tk.Button(self, text="Register an account", command=lambda: controller.show_frame("register_menu")).grid()
        tk.Button(self, text="Exit", bg="red", command=controller.destroy).grid()