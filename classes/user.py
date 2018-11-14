import random

class user:
    #initialization
    username=str
    password=str
    #TODO add more user account's details

    def user(self,name,pw): #constructor
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
