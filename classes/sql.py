import os
from mysql.connector import Error
import subprocess
subprocess.check_call(["python", '-m', 'pip', 'install', 'mysql-connector'])
#https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
import mysql.connector
from mysql.connector import (connection) #TODO reconsider which one use to


class sql:
    def __init__(self):
        self.username = str('project_cis020')
        self.pswd = str('8lGlvGTLqn')
        self.db_name = str('project_cis020')
        self.hname = str('busz.it')
        if(self.check_server()):
            self._connect()
        else:
            exit(9)
        #TODO reconsider below code
        err_success = 0
        err_fail = -1
        err_duplicate = 1062

    def check_server(self):
        self.response = os.system('ping -c 1 -m 1 '+str(self.hname))
        if self.response == 0: #if zero than successfully pinges
            return True
        else:                   #512 returned means no connection
            return False

    def _connect(self):
        try:
            self.connection = connection.MySQLConnection(user=self.username,database=self.db_name, password=self.pswd,
                                         host=self.hname)
        except Error as e:
            print(e)

    def _close(self, cursor):
        cursor.close()
        self.connection.close()

    def execute(self,command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        self._close(cursor)

    #TODO add method to check if database/table exists
    #TODO add try catch exception to all queries and executions

    def query(self,command): #TODO add close connection and error handling
        cursor = self.connection.cursor()
        cursor.execute(command)
        result = cursor.fetchall()
        self._close(cursor)
        return result

    def update(self,command): #also suitable for delete statments
        cursor = self.connection.cursor()    #TODO add close connection and error han
        cursor.execute(command)
        self.connection.commit() #apply changes
        self._close(cursor)