import random
import re
from classes import tool
from classes import data




class user:
    #TODO add more user account's details
    def isValidEmail(self, email):
        if len(email) > 7:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
                return True
        return False

    def __init__(self,name,pw): #constructor
        self.username=name
        self.password=pw
        self._auth()
        self._get_available_tools()

    def captcha(self): #TODO random operation generator
        #TODO consider if needed and implement to GUI
        a=random.randrange(10)
        b=random.randrange(10)
        result=a+b
        #TODO input validation
        userInput=input("Verification of your humanity, please calculate the result: "+str(a)+" + "+str(b)+" = ?")
        if(int(userInput)==int(result)):
            return True
        else:
            return False

    def _user_offered_tools(self):
        result = []
        for x in data.tools:
            if x.details['user_id'] == self.id:
                result.append(x)
        return result

    def _user_hired_tools(self):
        result = []
        for x in data.tools:
            if x.details['hiring_user']==self.id:
                result.append(x)
        return result

    def _get_available_tools(self):
        self.available_tools = []
        for tool in data.tools:
            if self.logged:
                if (tool.details['is_hired'] == False) and (tool.details['user_id'] != self.id):
                    self.available_tools.append(tool)
            else:
                self.available_tools=data.tools
                break


    def _auth(self): #TODO consider encrypting a password
        for y,x in data.users.items():
            if not x[0]==self.username:
                self.logged=False
            else:
                if x[1]==self.password:
                    self.logged= True
                    self.email=x[2]
                    self.full_name = x[3]
                    self.billing_address = x[4].rstrip('\n')
                    self.id = int(y)
                    self.offered_tools=self._user_offered_tools()
                    self.hired_tools= self._user_hired_tools()
                    return True
                else:
                    self.logged= False
                    return False
        return self.logged

    def getName(self):
        return str(self.username)

    def _userExists(self,mail): #checks if user with the same login or email already exists
        exist = False
        for y,x in data.users.items():
            if x[0] == self.username:
                exist = True
            else:
                if x[2]==mail:
                    exist = True
                else:
                    exist = False
        return exist

    def register(self,mail, f_name, b_address):
        if self.isValidEmail(mail):
            if not self._userExists(mail):
                self.email=mail
                self.full_name=f_name
                self.billing_address=b_address
                self.logged = True
                #TODO consider validating address
                file = open(data.get_users_file(len(data.users)),'w')
                file.write(self._file_format()) #create a user file
            else:
                print("user with the same login or email already exists")
        else:
            print("not valid email address")

    def _file_format(self):
        result = self.username+'#'      # 0) Username Login 	(String)
        result+= self.password+'#'      # 1) Password 		(String)
        result+= self.email+'#'         # 2) Email address 	(String)
        result+= self.full_name+'#'     # 3) Full Name 		(String)
        result+= self.billing_address.rstrip('\n')   # 4) Billing Address 	(String)
        return result


    #TODO add suspend/delete user account