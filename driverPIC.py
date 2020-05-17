from numpy import random
import numpy as np
from initial_distribution import initial_distribution_from_file,initial_distribution
from AssembleRHS import AssembleRHS
from details import detailed_output
from graphics import phase_space


#TODO 2. Get Matlab/Python examples of 2D/3D plasma to use as reference
#TODO 3. Step by step conversion to 3D using the same Numpy operations
#TODO 3.0.4. Evaluate all the quantities from the test of Prof.Sonnenddruecker (distr.func, energies).
#TODO 3.0.1. Organize the timestep as function, and send it to separate file
#TODO 3.0.2. Split the timestep
#TODO 3.0.2.1. Density function,returning also weights
#TODO 3.0.2.2. Field function
#TODO 3.0.2.3. Push function
#TODO 3.0.3. Make particle initial distribution accroding to given function
#TODO 3.0.3.1. start with the present two-stream, and get roughly the same

#TODO 3.1. Doing 3D at once, no 2D, both r and v 3D vectors
#TODO 3.2. Start with Ly,Lz being very small(0.1 Lx),Nx, Ny correspondinlgy,
# TODO3.3. y,z random vx,vz = 0
# TODO3.3. Observe the same two-stream instability
# TODO3.3.1. Evaluate all the quantities from the test of Prof.Sonnenddruecker (distr.func, energies).
# TODO3.4. Change main direction to Y, than to Z





L = 100      # domain of solution 0 <= x <= L
N = 20000    # number of electrons
J = 1000     # number of grid points
vb = 3       # beam velocity
dt = 0.1     # time-step (in inverse plasma frequencies)
tmax = 80.0  # simulation run from t = 0 to t = tmax

#initialize solution
r,v = initial_distribution(L,N,vb) #_from_file('r.txt','v.txt')
phase_space(0.0,dt,r,v)

t = 0.0
#evolve solution
while t<=tmax:
    # load r,v into a single vector
    solution_coeffs = np.concatenate((r,v))
    
    # take a 4th order Runge-Kutta timestep
    k1 = AssembleRHS(solution_coeffs,L,J,N)
    k2 = AssembleRHS(solution_coeffs + 0.5*dt*k1,L,J,N)
    k3 = AssembleRHS(solution_coeffs + 0.5*dt*k2,L,J,N)
    k4 = AssembleRHS(solution_coeffs + dt*k3,L,J,N)
    solution_coeffs = solution_coeffs + dt/6*(k1+2*k2+2*k3+k4)
    # unload solution coefficients
    r = solution_coeffs[0:N]
    v = solution_coeffs[N:2*N]
    # make sure all coordinates are in the range 0 to L
    r = r + L*(r<0) - L*(r>L)
    t = t + dt

    detailed_output(t,dt,solution_coeffs,k1,k2,k3,k4)
    phase_space(t,dt,r,v)

    print(t)



