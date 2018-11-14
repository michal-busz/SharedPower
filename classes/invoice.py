from datetime import datetime

class invoice:

    #variables
    totalAmount = float
    transportAmount = float
    toolsAmount = float
    lateFeeAmount = float
    dueDate = datetime()
    invoiceDate = datetime()

    #constants
    invoiceGeneration = 30 #day in month which all invoice will be generated
    insuranceFee = 5.00