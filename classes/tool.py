import datetime
import os
from classes import data

def str_to_bool(str):       #covert String to bool
    if str == 'False' or str == False:
        return False
    elif str == None or str=='None':
        return None
    else:
        return True

def str_to_date(str):       #covert String to datetime
    if str == None or str == 'None':
        return None
    temp = str.split('-')
    return datetime.date(int(temp[0]),int(temp[1]),int(temp[2]))

def str_to_ID(str):         #convert String to ID
    if str == None or str=='None':
        return None
    else:
        return int(str)

def str_to_UID(str):        #convert String to User ID & returns new ID if null
    if str == None or str=='None':
        return data.tool_id
    else:
        return int(str)

def str_to_cost(str):       #convert String to float(cost)
    if str == None or str=='None':
        return None
    else:
        return float(str)

def create_tool_details(name, price, user_id,  available_due, location,delivery_cost = 0, description="",
                        image=False, hired=False, delivery_to=None, delivery_from=None,
                        date_hire=None, id_hire=None, hired_to_date=None, return_date= None,
                        return_accepted= None, damaged=False, damage_cost=None, fault = None, is_half=None, id= None):
    details = {
        "delivery_cost": str_to_cost(delivery_cost),
        "name": str(name),
        "description": str(description),
        "price": float(price),
        "id": str_to_UID(id),
        "available_due": str_to_date(available_due),
        "is_hired":    str_to_bool(hired),
        "user_id":      str_to_ID(user_id),
        "location":     str(location),
        "is_damaged":   str_to_bool(damaged),
        "image":        str_to_bool(image),
        "is_deliveryTo":    str_to_bool(delivery_to),
        "is_deliveryFrom":  str_to_bool(delivery_from),
        "hire_from_date":   str_to_date(date_hire),
        "hiring_user":      str_to_ID(id_hire),
        "hired_to_date":    str_to_date(hired_to_date),
        "return_date":      str_to_date(return_date),
        "is_return_accepted":   str_to_bool(return_accepted),
        "damage_cost":      str_to_cost(damage_cost),
        "is_half_day":      str_to_bool(is_half),
        "fault_user":       str_to_bool(str(fault).rstrip("\n"))
    }
    return details

#creates details dict() for tool class

class tool:

    #constants
    maxHireDays = 3
    maxSearch = 6*7 #max weeks * 7 days
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
        # self.details['is_half_day']                         #is tool hired for a additional half of a day?

        self.details=details
        self.id=details['id']
        self.halfPrice = details['price']/2             #price for the half of a day
        self.lateFee = details['price']*2               #fee charged for every additional late day
        self.file = data.get_tools_file(self.id)        #gets path to tool's file


    def offer_tool(self): #creates tool's file & also suitable for updating existing files
        file = open(self.file,'w')
        file.write(self._file_format())

    def _file_format(self): #generates tool's file content
        result = str(self.details['name'])+'#'                       # 0) Tool Name 				(String)
        result += str(self.details['user_id'])+'#'              # 1) Owner user's ID 			(Integer)
        result += str(self.details['price']) +'#'               # 2) Price 				(Float)
        result += str(self.details['available_due'])+'#'        # 3) Date 'available due to' 		(datetime()) 	[datetime.today()]
        result += str(self.details['is_hired'])+'#'             # 4) Is tool hired? 			(Boolean) 	[False]
        result += str(self.details['location'])+'#'                  # 5) Location 				(String)
        result += str(self.details['delivery_cost'])+'#'        # 6) Delivery price 			(Float) 	[0.00]
        result += str(self.details['description']).rstrip('\n')+'#'  # 7) Long Description 			(String) 	[""]
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
        result += str(self.details['is_half_day'])+'#'
        result += str(self.details['fault_user'])               # 18) Is hiring user fault? 		(Boolean) 	[None]
        return result

    def hire_tool(self, usr_id, hired_to, half_day=False, delivery_to=False, delivery_from = False):    #hire tool action
        self.details['hiring_user'] = usr_id
        self.details['hired_to_date'] = hired_to
        self.details['is_deliveryTo'] = delivery_to
        self.details['is_deliveryFrom'] = delivery_from
        self.details['is_hired'] = True
        self.details['hire_from_date'] = self.getCurrentDate()
        self.details['is_half_day'] = half_day
        self.offer_tool()   # update necessary details

    def damage_tool(self,damage_description,isImage=False): # if owner think that tool is damaged action
        self.details['is_damaged'] = True
        self.details['is_return_accepted'] = False
        self.offer_tool() #update details
        data.damaged[str(self.id)] = damageDetails(self.id,damage_description,isImage,None)

    def return_damaged_tool(self,cost, flt_user): #executed only by insurance company
        self.details['damage_cost']=cost
        self.details['fault_user']=flt_user
        self.details['is_return_accepted']= True
        self.offer_tool()

    def remove_tool(self):              #remove tool action
        os.remove(self.file)
        #TODO consider removing item from GUI display after removing file

    def getCurrentDate(self):      #returns current date object
        return datetime.date.today()

    def return_tool(self): # only if return accepted by owner
        self.details['is_return_accepted']=True
        self.offer_tool()

    def request_return(self): #hiring user  request returning, owner should check tools condition and accept
        self.details['return_date'] = self.getCurrentDate()
        self.offer_tool()


class damageDetails:    #damaged tools object
    def __init__(self,id ,own_desc, isImage, company_resp):
        self.id = str_to_ID(id)
        self.owner_description = str(own_desc)
        self.isImageUploaded = str_to_bool(isImage)
        self.company_response = str_to_bool(company_resp)
        self.file = data.get_damaged_file(id)

    def _file_format(self):     #return files format for damaged tool
        result = str(self.owner_description)+"#"
        result+= str(self.isImageUploaded)+"#"
        result+= str(self.company_response)
        return result

    def post_damage(self): #creats and updates damaged tools file
        file = open(self.file, 'w')
        file.write(self._file_format())

    def completeCase(self, cost, flt_usr, response):    #used by insurance company to fisnish damaged tool queries
        self.company_response=response
        self.post_damage()
        for x in data.tools:
            if (x.id == self.id):
                x.return_damaged_tool(cost,flt_usr)
                break
