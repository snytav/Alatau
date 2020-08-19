from numpy import random
import numpy as np
from initial_distribution import initial_distribution_from_file,initial_distribution
from timestep import  timestep
from details import detailed_output
from graphics import phase_space
from GetDensity import GetDensity


#TODO 2. Get Matlab/Python examples of 2D/3D plasma to use as reference
#TODO 3. Step by step conversion to 3D using the same Numpy operations
#TODO 3.1. Change arythmetic operations in GetDensity to Numpy
#TODO 3.2. Check the 2D density with 2D suface plot of EDF

#TODO 3.0.2. Split the timestep
#TODO 3.0.2.1. Density function,returning also weights
#TODO 3.0.2.2. Field function
#TODO 3.0.2.3. Push function
#TODO 3.0.3. Make particle initial distribution accroding to given function
#TODO 3.0.3.1. start with the present two-stream, and get roughly the same
#TODO 3.0.4. Evaluate all the quantities from the test of Prof.Sonnenddruecker (distr.func, energies).
#TODO 3.1. Doing 3D at once, no 2D, both r and v 3D vectors
#TODO 3.2. Start with Ly,Lz being very small(0.1 Lx),Nx, Ny correspondinlgy,
# TODO3.3. y,z random vx,vz = 0
# TODO3.3. Observe the same two-stream instability
# TODO3.3.1. Evaluate all the quantities from the test of Prof.Sonnenddruecker (distr.func, energies).
# TODO3.4. Change main direction to Y, than to Z



#from test_density import test_density

#test_density()

L = 100      # domain of solution 0 <= x <= L
N = 20000    # number of electrons
J = 1000     # number of grid points
vb = 3       # beam velocity
dt = 0.1     # time-step (in inverse plasma frequencies)
tmax = 80.0  # simulation run from t = 0 to t = tmax

#initialize solution
#r,v = initial_distribution(L,N,vb) #_from_file('r.txt','v.txt')
r,v = initial_distribution_from_file('r.txt','v.txt')
rv = np.zeros((len(r),2))
rv[:,0] = r
rv[:,1] = v - np.min(v)
Lv = np.max(v) - np.min(v)
#edf = GetDensity( rv, [L,Lv], [J,J] )

phase_space(0.0,dt,r,v)

t = 0.0
#evolve solution
while t<=tmax:
    [r, v, k1, k2, k3, k4, solution_coeffs] = timestep(r,v,N,J,dt,L)
    t = t + dt
    detailed_output(t,dt,solution_coeffs,k1,k2,k3,k4)
    phase_space(t,dt,r,v)

    print(t)



