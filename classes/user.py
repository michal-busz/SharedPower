import random
import re
import datetime
from classes import data
from classes import invoice




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

    def _to_be_invoiced(self): #TODO check if it works correctly
        invoiced = []
        related_tools = self._related_tools()
        for inv in self.invoices:
            for x in inv.get_tools_ids():
                if x in related_tools:
                    invoiced.append(x)
        return list(set(related_tools) - set(invoiced))

    def _get_available_tools(self):
        self.available_tools = []
        for tool in data.tools:
            if self.logged:
                condition1= (tool.details['is_hired'] == False) and (tool.details['user_id'] != self.id)
                condition2= (tool.details['available_due']> datetime.date.today()) and (tool.details['is_damaged'] == False)
                if condition1 and condition2:
                    self.available_tools.append(tool)
            else:
                self.available_tools=data.tools
                break

    def _related_tools(self):
        result = []
        self.first_tool_date=datetime.date.today()
        for x in self.hired_tools:
            result.append(x)
            if (x.details['hired_to_date'] != None):
                if (self.first_tool_date > x.details['hired_to_date']):
                    self.first_tool_date = x.details['hired_to_date']
        for x in self.offered_tools:
            result.append(x)
            if (x.details['hired_to_date'] != None):
                if (self.first_tool_date > x.details['hired_to_date']):
                    self.first_tool_date = x.details['hired_to_date']
        return result

    def _auth(self): #TODO consider encrypting a password
        #TODO add insurance company login and activities
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
                    self.invoices = self._get_invoices()
                    self.tools_to_generate_inv = self._to_be_invoiced()
                    self._generate_invoices()
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

    def _get_invoices(self):
        result = []
        for x in data.invoices:
            if self.id == x.user_id:
                result.append(x)
        return result

    def _generate_invoices(self):
        last_invoice_date= datetime.date(1,1,1)
        for inv in self.invoices:
            if last_invoice_date < inv.generation_date:
                last_invoice_date= inv.generation_date
        if  last_invoice_date< datetime.date.today():
            if str(last_invoice_date) != '0001-01-01':
                to_generate = self._dates_to_generate(last_invoice_date)
            else:
                to_generate = self._dates_to_generate(self.first_tool_date)
            for year,x in to_generate.items():
                iterator = 0
                if x:
                    for month in x:
                        generation_date = datetime.date(int(year),int(month),30)
                        for t in self.tools_to_generate_inv:
                            if t.details['is_return_accepted'] == True and t.details['return_date'] < generation_date:
                                entries = self._generate_tool_invoice_entries(iterator,t)
                                uid = invoice.get_invoice_uid(self.id, month, year)
                                inv = invoice.invoice(entries,uid)
                                self.invoices.append(inv)
                                inv.generate_invoice()
                                self.tools_to_generate_inv.remove(t)

    def _dates_to_generate(self, date):
        result = dict()
        today = datetime.date.today()
        #date = date.replace(month=date.month+1) #TODO check if needed
        year_diffrence = today.year - date.year
        if year_diffrence:
            firsty_diffrence = 12 - date.month
            temp = []
            for x in range(firsty_diffrence + 1):
                temp.append(date.month + x)
            result[str(date.year)] = temp
            year_diffrence -= 1
            while (year_diffrence):
                temp = []
                for x in range(12):
                    temp.append(x + 1)
                result[str(date.year + year_diffrence)] = temp
                year_diffrence -= 1
            temp = []
            for x in range(today.month - 1):
                temp.append(x + 1)
            if today.day >= 30:
                temp.append(today.month)
            result[str(today.year)] = temp

        else:
            month_diffrence = today.month - date.month
            temp = []
            for x in range(month_diffrence):
                temp.append(date.month + x)
            if today.day >= 30:
                temp.append(today.month)
            result[str(date.year)] = temp
        return result

    def _generate_tool_invoice_entries(self,id, tool):
        result = []
        if tool.details['user_id'] == self.id:
            # tool
            amount = (tool.details['hired_to_date'] - tool.details['hire_from_date']).days
            amount = amount * tool.details['price']
            if (tool.details['is_half_day'] == True):
                amount += tool.halfPrice
            result.append(
                invoice.invoiceEntry(id, tool.id, tool.details['hire_from_date'], tool.details['hired_to_date'],
                                     tool.details['name'], (amount*-1)))
            id += 1
            # --------------------------------------------------
            # transportation
            if (tool.details['is_deliveryTo'] == True):
                result.append(
                    invoice.invoiceEntry(id, tool.id, tool.details['hire_from_date'], None, "Transportation To",
                                         (tool.details['delivery_cost']*-1)))
                id += 1
            if (tool.details['is_deliveryFrom'] == True):
                result.append(
                    invoice.invoiceEntry(id, tool.id, None, tool.details['hired_to_date'], "Transportation From",
                                         (tool.details['delivery_cost']*-1)))
                id += 1
            # --------------------------------------------------
            # lateFee
            if (tool.details['return_date'] > tool.details['hired_to_date']):
                late_days = (tool.details['return_date'] - tool.details['hired_to_date']).days
                feeAmount = late_days * tool.lateFee
                description = "Late Fee for " + str(late_days) + " days"
                result.append(
                    invoice.invoiceEntry(id, tool.id, tool.details['hired_to_date'], tool.details['return_date'],
                                         description, (feeAmount*-1)))
                id += 1
            # --------------------------------------------------
            # damage
            if (tool.details['is_damaged'] == True):
                if (tool.details['fault_user'] == True):
                    result.append(
                        invoice.invoiceEntry(id, tool.id, None, None, "Damage's cost", (tool.details['damage_cost']*-1)))
                    id += 1
        else:
            # tool
            amount = (tool.details['hired_to_date'] - tool.details['hire_from_date']).days
            amount = amount * tool.details['price']
            if (tool.details['is_half_day'] == True):
                amount += tool.halfPrice
            result.append(
                invoice.invoiceEntry(id, tool.id, tool.details['hire_from_date'], tool.details['hired_to_date'],
                                     tool.details['name'], amount))
            id += 1
            # --------------------------------------------------
            # insurance
            result.append(invoice.invoiceEntry(id, tool.id, None, None, "Insurance", 5.00))
            id += 1
            # --------------------------------------------------
            # transportation
            if (tool.details['is_deliveryTo'] == True):
                result.append(
                    invoice.invoiceEntry(id, tool.id, tool.details['hire_from_date'], None, "Transportation To",
                                         tool.details['delivery_cost']))
                id += 1
            if (tool.details['is_deliveryFrom'] == True):
                result.append(
                    invoice.invoiceEntry(id, tool.id, None, tool.details['hired_to_date'], "Transportation From",
                                         tool.details['delivery_cost']))
                id += 1
            # --------------------------------------------------
            # lateFee
            if (tool.details['return_date'] > tool.details['hired_to_date']):
                late_days = (tool.details['return_date'] - tool.details['hired_to_date']).days
                feeAmount = late_days * tool.lateFee
                description = "Late Fee for " + str(late_days) + " days"
                result.append(
                    invoice.invoiceEntry(id, tool.id, tool.details['hired_to_date'], tool.details['return_date'],
                                         description, feeAmount))
                id += 1

        return result

    #TODO add suspend/delete user account