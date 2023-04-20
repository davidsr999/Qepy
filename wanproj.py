import numpy as np 
from src.input import Qemodel
from src.stdin import Stdin
import sys


nfile = 'qe.nscf.in'
qemodel = Qemodel(nfile)


# Select atoms that are gonna contruct the axes
# (starting from atm1, atm2,...)
# atm2  atm8 atm5 (centre z-axis x-axis)
qemodel.obtain_axes_from_three_atoms(2,8,5)












