from mysql.connector import Error
import subprocess
subprocess.check_call(["python", '-m', 'pip', 'install', 'mysql-connector'])
#https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program

import mysql.connector
from mysql.connector import (connection) #TODO reconsider which one use to


class sql:
    def __init__(self):
        self.username = 'project_cis020'
        self.pswd = '8lGlvGTLqn'
        self.db_name = 'project_cis020'
        self.hname = 'busz.it'
        if(self.check_server()):
            self._connect()
        else:
            exit(9)
        #TODO reconsider below code
        err_success = 0
        err_fail = -1
        err_duplicate = 1062

    def check_server(self): #https://codereview.stackexchange.com/questions/75574/ping-function-in-python
        ret = subprocess.call(['ping', '-c', '2', '-W', '3', self.hname], stdout=open('/dev/null', 'w'),
                              stderr=open('/dev/null', 'w'))
        return ret == 0

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
        cursor = self.connection.cursor(dictionary=True)#cursor (MySQLdb.cursors.DictCursor)
        cursor.execute(command)
        result = cursor.fetchall()
        self._close(cursor)
        return result

    def update(self,command): #DELETE , INSERT
        cursor = self.connection.cursor()    #TODO add close connection and error han
        cursor.execute(command)
        self.connection.commit() #apply changes
        self._close(cursor)