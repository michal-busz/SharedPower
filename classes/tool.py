from datetime import datetime

class tool:

    #constants
    maxDays = 3
    maxSearch = 6*7 #max weeks * 7 days

    #TODO add transport fee and double fee for every additional day
    #TODO add date validation and check
    #initialization

    def __init__(self,name,desc,fprice,tFee,year,month,day,hired=False,hireDate=datetime().today(),peroid=0,tFrom=False,tTo=False):
        self.transportFee=tFee                          #transportation fee
        self.name = name                                #main name of the tool
        self.description = desc                         #description of the tool / additionall notes
        self.fullPrice = fprice                         #full price for the tool
        self.halfPrice = fprice/2                       #price for the half of a day
        self.lateFee = fprice*2                         #fee charged for every additional late day
        self.availableUntil = datetime(year,month,day)  #avability of the tool
        self.isHired = hired                            #is tool already hired?
        self.transportFrom = tFrom                      #is tranport From required?
        self.transportTo= tTo                           #is transport To required?


        if self.isHired:                                # if tool is hired, calculate until date
            self.hireDate = hireDate
            self.hiredUntil = datetime(self.hireDate.year, self.hireDate.month, self.hireDate.day+peroid)
        else:                                           #otherwise put None in variables
            self.hiredUntil = None
            self.hireDate = None
