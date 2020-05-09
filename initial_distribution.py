from numpy import random
import numpy as np

def initial_distribution(L,N,vb):
    #initialize solution
    t = 0
    np.random.seed(42)                              # seed the rand generator
    r = L*random.uniform(0,1,N)             # electron positions
#dlmwrite('r.txt',r,'delimiter','\t','precision','%25.15e');
    v1 = np.random.normal(-vb, 1, int(N/2))
    v2 = np.random.normal(vb,1, int(N/2))
    v = np.concatenate((v1, v2))     #dlmwrite('v.txt',v,'delimiter','\t','precision','%25.15e');
    return [r,v] 


def initial_distribution_from_file(rfname,vfname):
    r = np.loadtxt(rfname, delimiter='\n', unpack=True)
    v = np.loadtxt(vfname, delimiter='\n', unpack=True)
    return [r,v]