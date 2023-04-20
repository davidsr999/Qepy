import sys
import numpy as np 


class Stdin:
    def __init__(self, args=None):
        if args:
            self.args = args
        else:
            self.args = sys.argv
        self.runargs = False
        self.values = []
        self.options = []
        self.name = None
        self.mdir = None
        self.content = None
        self.Nargs = 0

        self.checkargs()
        if self.runargs:
            self.obtain_Nargs()
            self.get_optionsvalues()
            #self.print_options()
            #self.print_values()
        


    def checkargs(self):
        if len(self.args)>1:
            self.runargs = True
    def get_options(self):
        return self.options

    def get_values(self):
        return self.values
    def get_Nargs(self):
        return self.Nargs
    
    def get_Noptions(self):
        return len(self.options)

    def obtain_Nargs(self):
        if self.runargs:
            self.Nargs = len(self.args)

    def run(self):
        print("Stdin module run")

    def get_optionsvalues(self):
        for n in range(self.Nargs):
            if self.args[n][:2]=='--':
                self.options.append(self.args[n][2:])
                if n<self.Nargs-1:
                    if self.args[n+1][:2]!='--':
                        self.values.append(self.args[n+1])
                    else:
                        self.values.append(None)
                else:
                    self.values.append(None)
    def print_options(self):
        print(self.options)

    def print_values(self):
        print(self.values)

    def get_inputvalues(self):
        with open(self.fdir+self.name,'r') as f:
            self.content = f.readlines()




if __name__=='__main__':
    import sys
    args = sys.argv
    stdin = Stdin()
