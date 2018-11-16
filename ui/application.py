import tkinter as tk
from tkinter import font  as tkfont
from ui.welcome import welcome_menu
from ui.login import login_menu
from ui.register import register_menu

class App(tk.Tk):

    #def __init__(self,master):
        #self.master = master
        #self.frame= Frame()
        #self.frameInit()
        #self.welcome_menu()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Shared Power")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (welcome_menu, login_menu, register_menu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew") #IMPROTANT TO display properly

        self.show_frame("welcome_menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



