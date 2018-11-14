from datetime import datetime

class tool:

    #variables
    fullPrice= int
    halfPrice= int
    availableUntil= datetime()
    today = datetime.today()
    transportFrom = bool
    transportTo = bool

    #constants
    maxDays = 3
    maxSearch = 6*7 #max weeks * 7 days

    #TODO add transport fee and double fee for every additional day
    #TODO add date validation and check
    #initialization

    def tool(self,fprice,hprice,year,month,day,tFrom=False,tTo=False):
        self.fullPrice = fprice
        self.halfPrice = hprice
        self.availableUntil = datetime(year,month,day)
        self.transportFrom = tFrom
        self.transportTo= tTo