import tkinter as tk
from ui.welcome import welcome_menu
from ui.login import login_menu
from ui.register import register_menu
from ui.logged import logged_menu
from classes.user import user

class App(tk.Tk):
    usr = user
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #executes super's constructor

        self.title("Shared Power")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #container.grid_rowconfigure(0, weight=1) #TODO consider if required
        #container.grid_columnconfigure(0, weight=1) #TODO consider if required
        self.used_frames= {welcome_menu, login_menu, register_menu, logged_menu} #add all used frame classes
        self.frames = {} #stack all of frames

        for F in (self.used_frames):
            page_name = F.__name__ #saves name in order to easy-use
            frame = F(parent=container, controller=self) #creates each frame's object
            self.frames[page_name] = frame #stack frames in table
            frame.grid(row=0, column=0, sticky="nsew") #IMPROTANT TO display properly

        self.show_frame("welcome_menu")

    def show_frame(self, page_name): #page_name = text name of Frame to display
        frame = self.frames[page_name]
        frame.tkraise()  #moves frame to the top on the stack