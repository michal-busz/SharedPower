import os
import platform
from classes import tool
from classes import invoice

# data.py file reads all data from files and stores them in program's memory
def init():
    global slash    # stores OS slash
    global users    # stores all users objects
    global tools    # stores all tools objects
    global invoices # stores all invoices objects
    global images   # stores all images objects
    global damaged  # stores all damaged objects
    global current_user
    slash = _get_slash()            #fetch OS slash
    users = _get_users()            #fetch all users from files
    tools = _get_tools()            #fetch all tools from files
    invoices = _get_invoices()      #fetch all invoices from files
    images = _get_images()          #fetch all images from files
    damaged = _get_damaged_tools()  #fetch all damaged tools from files

def _get_slash():   #get correct slash depending on Operating System
    if (platform.system() == 'Windows'):
        return '\\'
    else:
        return '/'

def _get_users():   #return all users in dictionary
    ids = os.listdir(get_users_file())              #fetch all files in 'users' folder
    details = dict()
    for x in ids:
        detail = open(get_users_file(x)).readline() #get specific file's content (first line)
        temp = detail.split("#")                    #split content of the file
        details[str(x)]=temp                        #add user's details to dictionary
    return details

def _get_tools():   #return all tools in list
    ids = os.listdir(get_tools_file())              #fetch all files in 'tools' folder
    result = []
    for x in ids:
        detail = open(get_tools_file(x)).readline() #get specific file's content (first line)
        temp = detail.split("#")                    #split content of the file
        result.append(tool.tool(tool.create_tool_details(temp[0],temp[2],temp[1],temp[3],temp[5],temp[6],temp[7],temp[9],temp[4],temp[13],temp[14],temp[11],
                                               temp[10],temp[12],temp[15],temp[16],temp[8],temp[17],temp[19],temp[18],x)))
                                                    #create tool object and add it to the list
    return result

def _get_damaged_tools():   #return all damaged tools details
    ids = os.listdir(get_damaged_file())            #fetch all files in 'damaged' folder
    result = dict()
    for x in ids:
        detail = open(get_damaged_file(x)).readline()   #get specific file's content (first line)
        temp = detail.split("#")
        result[str(x)] = (tool.damageDetails(x,temp[0],temp[1],temp[2].rstrip('\n')))    #create damageDetails object and add it to the list
    return result

def _get_invoices():        #return all invoices
    ids = os.listdir(get_invoices_file())           #fetch all files in 'invoices' folder
    result = []
    for x in ids:                                   #process each file
        entries = []
        with open(get_invoices_file(x)) as f:       #use each line of the file
            temp = f.read().splitlines()            #read line and removes new line char
            for y in  temp:
                temp2 = y.split('#')
                entries.append(invoice.invoiceEntry(tool.str_to_ID(temp2[0]),tool.str_to_ID(temp2[1]),
                                                    tool.str_to_date(temp2[2]),
                                                    tool.str_to_date(temp2[3]),temp2[4],
                                                    tool.str_to_cost(temp2[5])))
                                                    #create invoiceEntry object and add it to the list of entries
        result.append(invoice.invoice(entries,x))   #add list of entries to the invoices list
    return result

def _get_images():          #return all images
    ids = os.listdir(get_images_file())             #fetch all files in 'images' folder
    details = dict()
    for x in ids:
        details[str(x)]=""
        #TODO implement handling image files (class etc.)
    return details

def get_tools_file(id=""):  #return path to the 'tools' folder
    return "data"+str(slash)+"tools"+str(slash)+str(id)

def get_users_file(id=""):  #return path to the 'users' folder
    return "data"+str(slash)+"users"+str(slash)+str(id)

def get_invoices_file(id=""): #return path to the 'invoices' folder
    return "data" + str(slash) + "invoices" + str(slash) + str(id)

def get_images_file(id=""):     #return path to the 'images' folder
    return "data" + str(slash) + "images" + str(slash) + str(id)

def get_damaged_file(id=""):    #return path to the 'damaged' folder
    return "data" + str(slash) + "damaged" + str(slash) + str(id)

'''
platform.system()   - https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
os.listdir()        - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
with x as y:        - https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
splitlines()        - https://www.w3schools.com/python/ref_string_splitlines.asp
'''