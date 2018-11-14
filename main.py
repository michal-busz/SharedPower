from classes.sql import sql
db = sql()
print(db.select("SELECT * FROM admin_project.test"))