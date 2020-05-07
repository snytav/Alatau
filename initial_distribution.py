from numpy import random
import numpy as np
import double_maxwellian

def initial_distribution(N,vb):
    #initialize solution
    t = 0
    np.rng(42)                              # seed the rand generator
    r = L*random.uniform(0,1,N)             # electron positions
#dlmwrite('r.txt',r,'delimiter','\t','precision','%25.15e');
    v = double_maxwellian(N,vb)             # electron velocities
#dlmwrite('v.txt',v,'delimiter','\t','precision','%25.15e');
    return [r,v] 


def initial_distribution_from_file(rfname,vfname):
    r = np.loadtxt(rfname, delimiter='\n', unpack=True)
    v = np.loadtxt(vfname, delimiter='\n', unpack=True)
    return [r,v]