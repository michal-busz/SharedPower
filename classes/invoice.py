from datetime import datetime
from classes.tool import tool

class invoice:

    #variables initial ideas
    totalAmount = float
    transportAmount = float
    toolsAmount = float
    lateFeeAmount = float
    dueDate = datetime()
    invoiceDate = datetime()

    #constants
    invoiceGenerationDay = 30 #CONST day in month which all invoice will be generated
    insuranceFee = 5.00 #CONST


class invoiceEntry:

    def __init__(self, item:tool):
        self.tool = item

    def totalCost(self):
        result = self.tool.n