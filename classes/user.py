import random
import re
from classes import sql
from classes import tool


def isValidEmail(email):
    if len(email) > 7:
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
            return True
    return False

class user:
    #TODO add more user account's details

    def __init__(self,name,pw): #constructor
        self.username=name
        self.password=pw
        self._auth()
        #TODO add authentication and SQL databases

    def captcha(self): #TODO random operation generator
        a=random.randrange(10)
        b=random.randrange(10)
        result=a+b
        #TODO input validation
        userInput=input("Verification of your humanity, please calculate the result: "+str(a)+" + "+str(b)+" = ?")
        if(int(userInput)==int(result)):
            return True
        else:
            return False

    def _db(self):
        return sql.sql()

    def _user_tools(self):
        qry= "SELECT * FROM tool WHERE usr_id='"+str(self.id)+"'"
        usr_tools= self._db().query(qry)
        result = []
        for x in usr_tools:
            '''y = tool.tool(x['name'],x['description'],x['price'],x['delivery_cost'],
                          x['available_due'],x['is_hired'],x['id'])'''
            result.append(tool(x))
        return result

    def _auth(self): #TODO consider encrypting a password
        qry="SELECT * FROM user_tbl WHERE login='"+self.username+"'"
        result = self._db().query(qry)
        if not result:
            self.logged=False
        else:
            if result[0]['password']==self.password:
                self.logged= True
                self.email=result[0]['email']
                self.full_name = result[0]['full_name']
                self.billing_address = result[0]['billing_address']
                self.id = result[0]['id']
                self.tools=self._user_tools()
            else:
                self.logged= False
        return self.logged

    def getName(self):
        return str(self.username)

    def _userExists(self,mail): #checks if user with the same login or email already exists
        qry = "SELECT * FROM user_tbl WHERE login='"+self.username+"'"
        result = self._db().query(qry)
        if not result: #no user with the same login
            qry2= "SELECT * FROM user_tbl WHERE email='"+mail+"'"
            result2 = self._db().query(qry2)
            if not result2: #no user with the same email
                return False
            else:
                return True
        else:
            return True

    def register(self,mail, f_name, b_address):
        if isValidEmail(mail):
            if not self._userExists(mail):
                self.email=mail
                self.full_name=f_name
                self.billing_address=b_address
                self.logged = True
                #TODO consider validating address
                qry = "INSERT INTO `user_tbl` (`id`, `login`, `password`, `email`, `full_name`, `billing_address`) " \
                      "VALUES (NULL, '"+self.username+"', '"+self.password+"', '"+mail+"'," \
                      " '"+f_name+"', '"+b_address+"');"
                self._db().execute(qry)  #TODO add try statment
            else:
                print("user with the same login or email already exists")
        else:
            print("not valid email address")

    def update_user_email(self,email): #TODO add validation before execution
        qry = "UPDATE `project_cis020`.`user_tbl` SET " \
              "`email` = '"+email+"' WHERE `user_tbl`.`login` = '"+self.username+"'; "
        self.email=email
        self._db().execute(qry)
        #TODO check if address exsists before changing

    def update_user_name(self,f_name):
        qry = "UPDATE `project_cis020`.`user_tbl` SET " \
              "`full_name` = '"+f_name+"' WHERE `user_tbl`.`login` = '"+self.username+"'; "
        self.full_name=f_name
        self._db().execute(qry)

    def update_user_password(self,pw): #TODO add function validating password complication
        qry = "UPDATE `project_cis020`.`user_tbl` SET " \
              "`password` = '"+pw+"' WHERE `user_tbl`.`login` = '"+self.username+"'; "
        self.password=pw
        self._db().execute(qry)

    def update_user_address(self,new_address):
        qry = "UPDATE `project_cis020`.`user_tbl` SET " \
              "`billing_address` = '" + new_address + "' WHERE `user_tbl`.`login` = '" + self.username + "'; "
        self.billing_address=new_address
        self._db().execute(qry)

