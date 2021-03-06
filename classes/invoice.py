import datetime
from classes import tool
from classes import data

class invoice:

    company_address= "69 Company Street, Luton LU1 1AS, UK"  #stores pernamently company address

    #constants
    invoiceGenerationDay = 30 #CONST day in month which all invoice will be generated

    def __init__(self, entries, uid):
        self._parse_uid(uid)                        #gather data from file's name
        self.entries = entries                      #assign invoice's entries
        self.total = self._calculate_total_cost()   #calculate total cost for the invoice
        self.file = data.get_invoices_file(uid)     #get invoice's file name
        self.uid = uid

    def generate_invoice(self):                 #creates invoice file & also suitable for updating invoice's file
        file = open(self.file,'w')
        for x in self.entries:
            file.write(x.file_format())

    def _calculate_total_cost(self):                #calculate total cost of each inovoice's entry
        result = 0.00
        for x in self.entries:
            result+= x.amount
        return result

    def get_tools_ids(self):                        #get related tools entries
        result = []
        for x in self.entries:
            result.append(x.tool_id)
        return set(result)
    def getText(self):
        result = ""
        for x in self.entries:
            result+= x.getText()+"\n"
        result+="\n Total amount = "+str(self.total)
        return result

    def _parse_uid(self,uid):                   #process file name to related details
        temp = uid.split('_')
        self.user_id = int(temp[0])
        self.generation_date = datetime.date(int(temp[2]),int(temp[1]),self.invoiceGenerationDay)


class invoiceEntry:     #stores single invoice's entry

    def __init__(self, id, tool_id, start_date, end_date, name, amount):
        self.tool_id = tool_id
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.amount = amount

    def getText(self):      #get invoice's entry output text
        result= str(self.id)+". "+self.name
        if self.start_date == None and self.end_date!= None:
            result+=" ("+self._reverseDate(self.end_date)+") | "
        elif self.start_date != None and self.end_date ==  None:
            result += " (" + self._reverseDate(self.start_date) + ") | "
        elif self.start_date == None and self.end_date == None:
            result+=" | "
        else:
            result+= " ("+self._reverseDate(self.start_date)+" - "
            result+= self._reverseDate(self.end_date)+")  | "
        result+=" Price: "+str(self.amount)
        return result

    def file_format(self):  #process details to file format
        result = str(self.id)+'#'+str(self.tool_id)+'#'
        result += str(self.start_date)+'#'
        result+= str(self.end_date)+'#'+self.name+'#'
        result+= str(self.amount)+'\n'
        return result

    def _reverseDate(self, date):   #reverse date format to DD-MM-YYYY
        temp = str(date).split('-')
        return temp[2]+"/"+temp[1]+"/"+temp[0]


def get_invoice_uid(id,month,year):     #generate invoice's name
    return str(id)+'_'+str(month)+'_'+str(year)