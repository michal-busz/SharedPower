import sys
import os

class data:

    def __init__(self):

        if not sys.platform == "linux":     #TODO rebuild to use windows first
            self.separator = "/"
        else:
            self.separator = "\\"       #windows separator

        self.path = os.getcwd()
