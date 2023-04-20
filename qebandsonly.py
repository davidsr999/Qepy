import sys
import os
from src.info import Help
import numpy as np 
from src.utils import get_nbnd, get_bands_from_qe 
from src.plot import * 
from src.readqeinputs import * 
import matplotlib.pyplot as plt 

run = True
helpinfo = Help()
commands = sys.argv
if len(commands)>1:
    commands = commands[1:]
    read_commands = True

# Read option's labels --label
option_list = []
lista = []
Ncom = len(commands)
for n in range(Ncom):
    if commands[n][2:]=='--':
        option_list.append(commands[n][:2])
        lista.append([commands[n][:2],commands[n+1]])



if 'help' in option_list:
    ind = option_list.index('help')
    helpinfo.initial()
    run = False
    



if run:    
    folder = "../"
    name = folder+'bandsplot.out.gnu'
    helpinfo.printmayhelp()
    bands = get_bands_from_qe(name)
    emin = -10
    emax = 2
    bndp1 = QeBandplot('QE monolayer nospin',folder)
    bndp1.bands = bands
    bndp1.kpts_special = [0.000, 0.3333, 0.9114, 1.5792]
    bndp1.kpts_special_lb = ['K', 'M', 'G', 'K']
    bndp1.ylim = [emin, emax]
    bndp1.qebandsonly()
    #bndp1.qebandsonlysave()
    bndp1.qebandsonlyshow()
