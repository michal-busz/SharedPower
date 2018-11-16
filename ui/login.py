import tkinter as tk

class login_menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # consider belowe code and lambda expression
        tk.Label(self, text="Username:").pack(side=tk.TOP)
        username = tk.Entry(self).pack(side=tk.TOP)
        tk.Label(self, text="Password:").pack()
        password = tk.Entry(self, show='*').pack()
        tk.Button(self, text="Back", command=lambda: controller.show_frame("welcome_menu")).pack(side=tk.LEFT)
        tk.Button(self, text="Login").pack(side=tk.RIGHT)  # TODO add action login