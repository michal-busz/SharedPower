import random
import re

class user:
    #variables
    username=str
    password=str
    logged=False
    #TODO add more user account's details

    def __init__(self,name,pw): #constructor
        self.username=name
        self.password=pw
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

    def isValidEmail(email):
        if len(email) > 7:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
                return True
        return False

    def auth(self):
        if(self.username=="test" and self.password=="test"): #add SQL authentication
            self.logged=True
        else:
            self.logged=False
        return self.logged