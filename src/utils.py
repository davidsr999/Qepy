import numpy as np
import os
import sys



def get_nbnd(emin,emax, bands, nbnd):
    nlist = []
    for n in range(nbnd):
        bmin, bmax = np.min(bands[n][:,1]), np.max(bands[n][:,1])
        if (emin<bmin) and (emax>bmax):
            nlist.append(n)
    return nlist

def check_file(name):
    if not  os.path.isfile(name):
        msg = "The name of the prefix.dat.gnu"+\
                "file for the bands plot is not found"
        msgfinal = "End of the calculation, revise the name of the file"
        print("\n"+msg)
        print(msgfinal)
        sys.exit()
   
    
        

def get_bands_from_qe(name):
    check_file(name)
    bands = []
    with open(name, 'r') as f:
        lfile = f.readlines()
        f.close()

    N = len(lfile)
    band = []
    onlyblock = True
    for i in range(N):
        line = lfile[i].strip().split()
        if len(line)>0:
            band.append(np.array([float(x) for x in line]))
        else:
            bands.append(np.array(band))
            band = []
            onlyblock = False
    if onlyblock:
        return band
    else:
        return bands



