import matplotlib.pyplot as plt 
from .readqeinputs import Qeinput
import numpy as np 
import os 



class QeBandplot:
    def __init__(self,title, folder):
        self.fig = plt.figure(figsize=(8,6))
        self.ax = self.fig.add_subplot()
        self.folder = folder # folder where all inputs
        # outputs from QE are
        self.title = title
        self._xlim = None 
        self._ylim = None
        self._bands = None
        #self.title = title 
        #self.kpts_special = None
        #self.kpts_special_lb = None
        self.c = ["#8EE5EE","#7AC5CD", "#FF6103", "#ED9121", 
                "#7FFF00"]


    #----- title
    def title(self):
        return self.title 
    def set_title(self, value):
        self.title = value

    #-----kpts_special
    def kpts_special(self):
        return self.kpts_special
    def set_kpts_special(self, value):
        self.kpts_special  = value
    
    #----- kpts_special_lb
    def kpts_special_lb(self):
        return self.kpts_special_lb 
    def set_kpts_special_lb(self, value):
        self.set_kpts_special_lb = value
        jjj
    #----- xlim
    @property
    def xlim(self):
        return self._xlim 
    @xlim.setter
    def xlim(self, value):
        if len(value)!=2:
            raise AttributeError("Invalid xlim, must be array or list like\
            [a,b]")
        self._xlim = value

    #----- ylim
    @property
    def ylim(self):
        return self._ylim 
    @xlim.setter
    def ylim(self, value):
        if len(value)!=2:
            raise AttributeError("Invalid xlim, must be array or list like\
            [a,b]")
        self._ylim = value


    @property
    def bands(self):
        return self._bands
    @bands.setter
    def bands(self, value):
        self._bands = value
        self.get_nbnd()
        self.get_kpts_from_bands()
        self.obtain_array_bands()

    def qebandsonly(self):
        self.ax.set_xlim(self._xlim)
        self.ax.set_ylim(self._ylim)
        self.ax.set_title(self.title)
        self.plot_vertical_lines_spkpts()
        self.plot_efermi()
        for n in range(self.nbnd):
            self.ax.plot(self.kpts, self.bandsn[n,:], color=self.c[2])
        #self.show()
        
    def plot_efermi(self):
        readnscf = Qeinput(self.folder+"qe.nscf.out")
        readnscf.run()
        self.efermi = readnscf.efermi
        del readnscf
        self.ax.axhline(y=self.efermi, color='black', alpha=0.4,
        ls='--')

    def get_nbnd(self):
        self.nbnd = len(self.bands)

    def get_nkpts(self):
        self.nkpts = len(self.kpts) # number of kpts

    def get_kpts_from_bands(self):
        self.kpts = self.bands[0][:,0] # list of kpts 
        self.get_nkpts() # number of kpts

    def obtain_array_bands(self):
        bandsn = np.empty((self.nbnd,self.nkpts))
        for n in range(self.nbnd):
            bandsn[n,:] = self.bands[n][:,1]
        self.bandsn = bandsn

    def plot_vertical_lines_spkpts(self):
        for i in range(len(self.kpts_special)):
            self.ax.axvline(x=self.kpts_special[i], color='black',alpha=0.2, ls='--')
        self.ax.set_xticks(self.kpts_special)
        self.ax.set_xticklabels(self.kpts_special_lb)

    def qebandsonlysave(self,name=None):
        if name:
            plt.savefig(name)
        else:
            plt.savefig(self.title)

    def qebandsonlyshow(self):
        plt.show()
