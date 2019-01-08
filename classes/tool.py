import datetime
import os
from classes import data

def create_tool_details(name, price, user_id,  available_due, location,delivery_cost = 0, description="",
                        image=False, hired=False, delivery_to=False, delivery_from=False,
                        date_hire=None, id_hire=-1, hired_to_date=False, return_date= None,
                        return_accepted= True, damaged=False, damage_cost=0, fault = None, id= None):
    details = {
        "delivery_cost": float(delivery_cost),
        "name": str(name),
        "description": str(description),
        "price": float(price),
        "id": int(id),
        "available_due": available_due,
        "is_hired":    bool(hired),
        "user_id":      int(user_id),
        "location":     str(location),
        "is_damaged":   bool(damaged),
        "image":        bool(image),
        "is_deliveryTo":    bool(delivery_to),
        "is_deliveryFrom":  bool(delivery_from),
        "hire_from_date":   date_hire,
        "hiring_user":      int(id_hire),
        "hired_to_date":    hired_to_date,
        "return_date":      return_date,
        "is_return_accepted":   return_accepted,
        "damage_cost":      float(damage_cost),
        "fault_user":       bool(str(fault).rstrip("\n"))
    }
    return details

class tool:

    #constants
    maxDays = 3
    maxSearch = 6*7 #max weeks * 7 days

    #TODO double fee for every additional day
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
        # self.details['is_deliveryTo']                       #is delivery to hiring user purchased?
        # self.details['is_deliveryFrom']                     #is delivery from hiring user purchased?
        # self.details['hire_from_date']                      #tool hired on date
        # self.details['hiring_user']                         #ID of hiring user
        # self.details['hired_to_date']                       #tool hired to date
        # self.details['return_date']                         #tool return date
        # self.details['is_return_accepted']                  #is return accepted by owner?
        # self.details['damage_cost']                         #cost of damage
        # self.details['fault_user']                          #is hiring user fault of damage?

        self.details=details
        self.id=details['id']
        self.halfPrice = details['price']/2             #price for the half of a day
        self.lateFee = details['price']*2               #fee charged for every additional late day
        self.file = data.get_tools_file(self.id)


    def offer_tool(self, new=False): #also suitabkle for updating details of the tool
        #TODO consider increasing ID of a new tool
        file = open(self.file,'w')
        file.write(self._file_format())

    def _file_format(self):
        result = self.details['name']+'#'                       # 0) Tool Name 				(String)
        result += str(self.details['user_id'])+'#'              # 1) Owner user's ID 			(Integer)
        result += str(self.details['price']) +'#'               # 2) Price 				(Float)
        result += str(self.details['available_due'])+'#'        # 3) Date 'available due to' 		(datetime()) 	[datetime.today()]
        result += str(self.details['is_hired'])+'#'             # 4) Is tool hired? 			(Boolean) 	[False]
        result += self.details['location']+'#'                  # 5) Location 				(String)
        result += str(self.details['delivery_cost'])+'#'        # 6) Delivery price 			(Float) 	[0.00]
        result += self.details['description'].rstrip('\n')+'#'  # 7) Long Description 			(String) 	[""]
        result += str(self.details['is_damaged'])+'#'           # 8) Is tool damaged? 			(Boolean) 	[False]
        result += str(self.details['image'])+'#'                # 9) Is image attached? 			(Boolean) 	[False]
        result += str(self.details['hiring_user'])+'#'          # 10) Hiring user's ID 			(Integer) 	[-1]
        result += str(self.details['hire_from_date'])+'#'       # 11) Hiring date 			(datetime()) 	[None]
        result += str(self.details['hired_to_date'])+'#'        # 12) Hired to date 			(datetime()) 	[None]
        result += str(self.details['is_deliveryTo'])+'#'        # 13) Is delivery to purchased? 		(Boolean) 	[False]
        result += str(self.details['is_deliveryFrom'])+'#'      # 14) Is return delivery required? 	(Boolean) 	[False]
        result += str(self.details['return_date'])+'#'          # 15) Return date 			(datetime()) 	[None]
        result += str(self.details['is_return_accepted'])+'#'   # 16) Is return accepted? 		(Boolean) 	[None]
        result += str(self.details['damage_cost'] )+'#'         # 17) Damage cost				(Float) 	[-1]
        result += str(self.details['fault_user'])               # 18) Is hiring user fault? 		(Boolean) 	[None]
        return result

    def hire_tool(self, usr_id, hired_to, delivery_to=False, delivery_from = False):
        self.details['hiring_user'] = usr_id
        self.details['hired_to_date'] = hired_to
        self.details['is_deliveryTo'] = delivery_to
        self.details['is_deliveryFrom'] = delivery_from
        self.details['is_hired'] = True
        self.details['hire_from_date'] = self._getCurrentDate()
        self.offer_tool()   # update necessary details
        #TODO add invoice entry

    def damage_tool(self): # if owner think that tool is damaged
        self.details['is_damaged'] = True
        self.details['is_return_accepted'] = False
        self.offer_tool() #update details
        #TODO consider return date value

    def remove_tool(self):
        os.remove(self.file)
        #TODO consider removing item from GUI display after removing file

    def _getCurrentDate(self):
        return datetime.datetime.day(datetime.datetime.today())

    def return_tool(self): # only if return accepted by owner
        #TODO consider changing is_hired value
        self.details['is_return_accepted']=True
        self.offer_tool()

    def request_return(self): #hiring request returning, owner should check tools condition and accept
        self.details['return_date'] = self._getCurrentDate()
        #TODO calculate late return fee
        #TODO add validation of returning date

#TODO  add insurance company methods