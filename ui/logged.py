import tkinter as tk

class logged_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Button(self, text="Search for tools").pack()
        self.loginBt = tk.Button(self, text="Logout", command=self.logout).pack()
        tk.Button(self, text="Exit", bg="red", command=controller.destroy).pack()
        self.banner = tk.Label(self)

    def logged(self):
        self.banner["text"]="You are logged in as "+self.controller.usr.username
        self.banner.pack()

    def logout(self):
        self.controller.frames["login_menu"].username.delete(0, 'end')
        self.controller.frames["login_menu"].password.delete(0, 'end')
        self.controller.frames["login_menu"].invalidLogin.pack_forget()
        self.controller.show_frame("welcome_menu")