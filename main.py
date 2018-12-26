'''from ui.application import App

app = App() #Tkinter.Tk object
app.mainloop() #starts'''
'''from classes import user
test = user.user("test2","test3")'''

from classes import tool
details = tool.create_tool_details("Tool",14.5,3,8,"2019-01-12","Luton","test")
test = tool.tool(details)
test.offer_tool()