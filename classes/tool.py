from datetime import datetime
from classes import sql

def create_tool_details(name, price, user_id, delivery_cost, available_due, location, description="",  image=""):
    details = {
        "delivery_cost": delivery_cost,
        "name": name,
        "description": description,
        "price": price,
        "id": None,
        "available_due": available_due,
        "is_hired":    0,
        "user_id":      user_id,
        "location":     location,
        "is_damaged":   0,
        "image":        image
    }
    return details

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
        qry = "SELECT * FROM hired_tool WHERE tool_id='"+str(self.id)+"'"
        result = self._db().query(qry)
        self.hiring_user= result[0]['usr_id']
        self.hireDate = result [0]['hire_date']
        self.hiredTo = result[0]['hired_to']
        self.deliveryTo = result[0]['delivery']
        self.deliveryFrom = result[0]['delivery_return']

    def _get_damaged_info(self):
        qry = "SELECT * FROM damaged_tool WHERE tool_id='"+str(self.id)+"'"
        result = self._db().query(qry)
        self.damage_cost = result[0]['cost']
        self.damage_fault = result[0]['fault'] #id of user charged for the damage

    def _db(self):
        return sql.sql()

    def db_update_tool_info(self):
        qry= "UPDATE `project_cis020`.`tool` SET `name` = '"+self.details['name']+"'," \
             " `price` = '"+self.details['price']+"', `available_due` = '"+str(self.details['available_due']) +"', " \
             "`is_hired` = '"+self.details['is_hired']+"', `location` = '"+self.details['location']+"', " \
             "`delivery_cost` = '"+self.details['delivery_cost']+"', `description` = '"+self.details['description']+"'," \
             " `is_damaged` = '"+self.details['is_damaged']+"', `image` = '"+self.details['image']+"' WHERE `tool`.`id` = "+str(self.id)+";"
        self._db().execute(qry)

    def offer_tool(self):
        qry = "INSERT INTO `project_cis020`.`tool` (`id`, `name`, `usr_id`, `price`, `available_due`, `is_hired`, `location`, `delivery_cost`, `description`, `is_damaged`, `image`) VALUES (NULL, " \
              "'"+self.details['name']+"', '"+str(self.details['user_id'])+"', '"+str(self.details['price'])+"', " \
              "'"+str(self.details['available_due'])+"', '0', '"+self.details['location']+"', '"+str(self.details['delivery_cost'])+"'," \
              " '"+self.details['description']+"', '0', '"+self.details['image']+"');"
        self._db().execute(qry)

    def hire_tool(self):
        qry = "INSERT INTO `project_cis020`.`hired_tool` (`tool_id`, `usr_id`, `hire_date`, `hired_to`, `delivery`, `delivery_return`) VALUES " \
              "('"+self.id+"', '"+self.hiring_user+"', '2018-12-25', '2018-12-28', '1', '0');"


    def damage_toll(self):
        qry = "INSERT INTO `project_cis020`.`damaged_tool` (`tool_id`, `cost`, `fault`) VALUES ('1', '20', '2'); "