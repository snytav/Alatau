import numpy as np
from GetDensity import GetDensity
from Poisson1D import Poisson1D
from GetElectric import GetElectric

def AssembleRHS( solution_coeffs, L, J,N ):
    r = solution_coeffs[0:N]    
    v = solution_coeffs[N:2*N]
    r = r + L*(r<0) - L*(r>L)
    #  Calculate electron number density
    ne = GetDensity( r, L, J )
    # Solve Poisson equation
    n0 = N/L
    rho = ne/n0 - 1
    phi = Poisson1D( rho, L )
    # Calculate electric field
    E = GetElectric( phi, L )
    # equations of motion
    dx = L/J
    js = np.floor(r/dx)
    ys = r/dx - (js)
    j = np.mod(js, J) + 1
    j = j + J * (j < 0) - J * (j >= J)
    js_plus_1 = j
    Efield = E[js.astype(int)]*(1-ys) + E[js_plus_1.astype(int)]
    np.savetxt('ef.txt', Efield, delimiter='\n', fmt='%15.5e')
    rdot = v
    vdot = -Efield
    RHS = np.concatenate((rdot, vdot))
    return RHS

