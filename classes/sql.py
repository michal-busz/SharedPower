import mysql.connector
class sql:
    hostname="busz.it"
    db_name="admin_project"
    db_username="admin_project"
    db_password="mFObHQHSgv"
    db= None

    def __init__(self):
        self.db=mysql.connector.connect(host=self.hostname,user=self.db_username,passwd=self.db_password)
        print(self.db)

    def query(self,query): #queries with results e.g. SELECT
        cursor=self.db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def execute(self,query): #suitable for: INSERT,UPDATE,DELETE
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        print(cursor.rowcount," rows executed") #internal note

        #TODO error handling, exceptions throwing

