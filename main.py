'''from ui.application import App

app = App() #Tkinter.Tk object
app.mainloop() #starts'''
'''from classes import user
test = user.user("test2","test3")'''
from classes import data
from classes import user
data.init()
test = user.user("login","password")