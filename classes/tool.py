from datetime import datetime

class tool:
    fullPrice= int
    halfPrice= int
    availableUntil= datetime()
    today = datetime.today()
    maxDays = 3
    #initialization

    def tool(self,fprice,hprice,year,month,day):
        fullPrice = fprice
        halfPrice = hprice
        availableUntil = datetime(year,month,day)