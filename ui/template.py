import tkinter as tk

class template(tk.Frame): #required to inherit tk.Frame
    def __init__(self, parent, controller): #parent= master frame , controller= tk.Tk object to switch windows
        tk.Frame.__init__(self, parent)             #execute super constructor
        self.controller = controller                #required to use controller.show_frame()
        tk.Button(self, text="Exit", bg="red",fg="red", command=lambda: controller.destroy()).pack()
        #some example button, lamba as example of methods with arguments