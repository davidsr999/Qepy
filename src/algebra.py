import numpy as np 



def get_angle_v1v2(v1,v2):
    v1n = np.linalg.norm(v1)
    v2n = np.linalg.norm(v2)
    cosangle = np.dot(v1,v2)/(v1n*v2n)
    return np.arccos(cosangle)


def rad_to_deg(rad):
    return rad*180/np.pi

def deg_to_rad(deg):
    return deg*np.pi/180


def get_perpendicular_v(v1,v2):
    m = np.cross(v1,v2)
    return m/np.linalg.norm(m)




