'''from classes import data
from classes import user
data.init()
test = user.user("login","password")'''

from classes import data
from ui import full_login_and_regis
data.init()
app = full_login_and_regis.Main_win()
app.mainloop()