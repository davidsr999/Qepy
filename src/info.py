import numpy as np 






class Help:
    def __init__(self):
        self.initial_message = "These are the available options for this\
                program." 
        self.msg2 = "If you want to normally run the qebandsonly.py program \
                do not write --help in the command line."
        self.msg3 = "If you need help with this program, write \
                qebandsonly.py --help"


    def initial(self):
        print(self.initial_message)
        print(self.msg2)

    def printmayhelp(self):
        print(self.msg3)
