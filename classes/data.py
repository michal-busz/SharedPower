import os
import platform
from classes import tool
from classes import invoice

def init():
    global slash
    global users
    global tools
    global invoices
    global images
    slash = _get_slash()
    users = _get_users()
    tools = _get_tools()
    invoices = _get_invoices()
    images = _get_images()

def _get_slash():
    if (platform.system() == 'Linux'):
        return '/'
    else:
        return '\\'

def _get_users():
    ids = os.listdir(get_users_file())
    details = dict()
    for x in ids:
        detail = open(get_users_file(x)).readline()
        temp = detail.split("#")
        details[str(x)]=temp
    return details

def _get_tools():
    ids = os.listdir(get_tools_file())
    result = []
    for x in ids:
        detail = open(get_tools_file(x)).readline()
        temp = detail.split("#")
        result.append(tool.tool(tool.create_tool_details(temp[0],temp[2],temp[1],temp[3],temp[5],temp[6],temp[7],temp[9],temp[4],temp[13],temp[14],temp[11],
                                               temp[10],temp[12],temp[15],temp[16],temp[8],temp[17],temp[19],temp[18],x)))
    return result

def _get_invoices():
    ids = os.listdir(get_invoices_file())
    result = []
    for x in ids:
        entries = []
        with open(get_invoices_file(x)) as f:
            temp = f.read().splitlines()
            for y in  temp:
                temp2 = y.split('#')
                entries.append(invoice.invoiceEntry(tool.str_to_ID(temp2[0]),tool.str_to_ID(temp2[1]),
                                                    tool.str_to_date(temp2[2]),
                                                    tool.str_to_date(temp2[3]),temp2[4],
                                                    tool.str_to_cost(temp2[5])))
        result.append(invoice.invoice(entries,x))
    return result

def _get_images():
    ids = os.listdir(get_images_file())
    details = dict()
    for x in ids:
        details[str(x)]=""
        #TODO implement handling image files (class etc.)
    return details

def get_tools_file(id=""):
    return "data"+str(slash)+"tools"+str(slash)+str(id)

def get_users_file(id=""):
    return "data"+str(slash)+"users"+str(slash)+str(id)

def get_invoices_file(id=""):
    return "data" + str(slash) + "invoices" + str(slash) + str(id)

def get_images_file(id=""):
    return "data" + str(slash) + "images" + str(slash) + str(id)

def get_damaged_file(id=""):
    return "data" + str(slash) + "damaged" + str(slash) + str(id)