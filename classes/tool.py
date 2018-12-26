from datetime import datetime
from classes import sql

class tool:

    #constants
    maxDays = 3
    maxSearch = 6*7 #max weeks * 7 days

    #TODO add transport fee and double fee for every additional day
    #TODO add date validation and check
    #initialization

    def __init__(self,details):
        # self.details['delivery_cost']                       #transportation fee
        # self.details['name']                                #main name of the tool
        # self.details['description']                         #description of the tool / additionall notes
        # self.details['price']                               #full price for the tool
        # self.details['available_due']                       #avability of the tool
        # self.details['is_hired']                            #is tool already hired?
        # self.details['user_id']                             #owner user's id
        # self.details['location']                            #location where tool is available
        # self.details['is_damaged']                          #is tool damaged?
        # self.details['image']                               #location of the image or image itself

        self.details=details
        self.id=details['id']
        self.halfPrice = details['price']/2             #price for the half of a day
        self.lateFee = details['price']*2               #fee charged for every additional late day

        if self.details['is_hired'] == 1:
            self._get_hired_info()

        if self.details['is_damaged'] == 1:
            self._get_damaged_info()

    def _get_hired_info(self):
        qry = "SELECT * FROM hired_tool WHERE tool_id='"+self.id+"'"
        result = self._db().query(qry)
        self.hiring_user= result[0]['usr_id']
        self.hireDate = result [0]['hire_date']
        self.hiredTo = result[0]['hired_to']
        self.deliveryTo = result[0]['delivery']
        self.deliveryFrom = result[0]['delivery_return']

    def _get_damaged_info(self):
        qry = "SELECT * FROM damaged_tool WHERE tool_id='"+self.id+"'"
        result = self._db().query(qry)
        self.damage_cost = result[0]['cost']
        self.damage_fault = result[0]['fault'] #id of user charged for the damage

    def _db(self):
        return sql.sql()

