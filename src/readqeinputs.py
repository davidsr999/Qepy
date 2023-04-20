import numpy as np 
import os
import sys



class Qeinput:
    def __init__(self,fname):
        self.name = fname
        self.inquire_file()
        self.nscf_out = None
        self.Nnscf_out = None 
        self.efermi = None # eV


    def inquire_file(self):
        check = os.path.isfile(self.name)
        if not check:
            print("\n\n   Such file ("+self.name+") does not exist, revise it!!")
            print("Cannot read output of nscf")
            sys.exit()

    def read_nscf_out(self):
        with open(self.name, 'r') as f:
            self.nscf_out = f.readlines()
            self.Nnscf_out = len(self.nscf_out)

    def read_efermi(self):
        pattern = ['fermi']
        Np = len(pattern)
        for n in range(self.Nnscf_out):
            line = self.nscf_out
            if (pattern[0] in line[n].lower()): 
                self.efermi = float(line[n].strip().split()[-2])

    def run(self):
        self.read_nscf_out()
        self.read_efermi()
        self.delete_nscf_out()
            


    def delete_nscf_out(self):
        del self.nscf_out


    def runtest(self):
        print("\   Program to read nscf.out file")
        self.read_nscf_out()
        self.read_efermi()
        self.delete_nscf_out()
        print("The Fermi energy is: "+str(self.efermi))










if __name__ == '__main__':
    file = "../../qe.nscf.out"
    test = Qeinput(file)
    test.runtest()


