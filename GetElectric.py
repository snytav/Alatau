import numpy as np
def GetElectric( phi, L ):
    #Calculate electric field from potential 
    J = len(phi)
    dx = L/J 
#     E(j) = (phi(j-1) - phi(j+1)) / (2*dx) 
    E = (np.roll(phi,1)-np.roll(phi,-1))/(2*dx)
    return E
