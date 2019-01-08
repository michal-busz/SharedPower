import os
import platform
from classes import tool


def init():
    global slash
    global users
    global tools
    global invoices
    slash = _get_slash()
    users = _get_users()
    tools = _get_tools()

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
                                               temp[10],temp[12],temp[15],temp[16],temp[8],temp[17],temp[18],x)))
    return result

def get_tools_file(id=""):
    return "data"+str(slash)+"tools"+str(slash)+str(id)

def get_users_file(id=""):
    return "data"+str(slash)+"users"+str(slash)+str(id)