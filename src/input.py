import numpy as np 
from .stdin import Stdin
from .algebra import get_angle_v1v2, deg_to_rad, rad_to_deg
from .algebra import get_perpendicular_v 



class Qemodel:
    def __init__(self,name=None,fdir=None):
        self.name = name
        self.dir = fdir
        self.content = None
        self.atomic_positions = []
        self.atoms = []

        # axes for the local 
        # basis projection in Wannier90
        self.localbasis = None 


        self.get_options()
        self.read_input()
        self.get_atomic_positions()
        self.delete_read_content()
        self.print_atmpos()
        self.obtain_atoms()
        self.print_atoms()

        self.ntyp = len(self.atoms)


        



    def get_options(self):
        args = Stdin()
        options = args.get_options()
        values = args.get_values()
        Nopt = args.get_Noptions()

    def read_input(self):
        with open(self.name, 'r') as f:
            self.content = f.readlines()

    def delete_read_content(self):
        del self.content



    def get_atomic_positions(self):
        pattern = "ATOMIC_POSITIONS"
        N = len(self.content)
        for n in range(N):
            if "nat" in self.content[n]:
                self.nat = self.content[n].strip().split()[-1]
                self.nat = int(self.clean_string(self.nat))
            if pattern in self.content[n]:
               nn = n 
        for n in range(self.nat):
            l = self.content[n+nn+1].strip().split()
            l[1:] = [float(x) for x in l[1:]]
            self.atomic_positions.append(l)


    def print_atmpos(self):
        for i in range(self.nat):
            print(self.atomic_positions[i])
    def print_atoms(self):
        print(self.atoms)


    def obtain_atoms(self):
        self.atoms.append(self.atomic_positions[0][0])
        old = self.atoms[0]
        for i in range(1,self.nat):
            new = self.atomic_positions[i][0]
            if old!=new:
                self.atoms.append(new)
                old = new


    def obtain_axes_from_three_atoms(self,atm1=None,atm2=None,atm3=None):
        print("Obtain axes with origin in atm1, atm2 as z and atm3 as x")
        if not atm1 and atm2 and atm3:
            print("Wrong arguments, try againg")
            sys.exit()
        atm1 += -1
        atm2+= -1
        atm3 += -1

        vatm1 = np.array(self.atomic_positions[atm1][1:])
        vatm2 = np.array(self.atomic_positions[atm2][1:])
        vatm3 = np.array(self.atomic_positions[atm3][1:])
        print("atm1: ",self.atomic_positions[atm1])
        print("atm2: ",self.atomic_positions[atm2])
        print("atm3: ",self.atomic_positions[atm3])
        bz = vatm2-vatm1
        bx = vatm3-vatm1
        print("Original axes:")
        print("bz = ",bz)
        print("bx = ",bx)
        bx_to_bz = get_angle_v1v2(bx,bz)

        print("angle axes initial: ", rad_to_deg(bx_to_bz))
        print("Let's obtain orthogonal axes fixing z and correcting x")


        gt90 = bx_to_bz>90
        m = get_perpendicular_v(bz,bx)
        # Check bz*m = 0 and bx*m = 0
        print("angle(bz,m) = ",get_angle_v1v2(bz,m)*180/np.pi)
        print("angle(bx,m) = ",get_angle_v1v2(bx,m)*180/np.pi)

        c1 = (bz[2]*m[1]-bz[1]*m[2])/(bz[0]*m[1]-bz[1]*m[0])
        c2 = (bz[2]*m[0]-bz[0]*m[2])/(bz[1]*m[0]-bz[0]*m[1])
        vx3 = 1/np.sqrt(1+c1**2+c2**2) 
        vx1 = -vx3*c1
        vx2 = -vx3*c2
        vx = np.array([vx1,vx2,vx3])
        angle_vxbx = get_angle_v1v2(bx,vx)

        if angle_vxbx>np.pi/2:
            vx = -vx

        vz = bz
        print("New axes are:")
        print("vx = ", vx)
        print("vz = ", vz)
        print("angle(vx,vz) = ", get_angle_v1v2(vx,vz)*180/np.pi)
        print("angle(vx,m) = ", get_angle_v1v2(vx,m)*180/np.pi)
        print("angle(vx,bx) = ", get_angle_v1v2(vx,bx)*180/np.pi)
        self.localbasis = [vx,vz]


            



        



    def clean_string(self,string):
        N = len(string)
        new = ''
        for n in range(N):
            if not string[n] in [',', '.', '[', ']', '-']:
                new += string[n]
        return new


