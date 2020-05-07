import numpy as np
def Poisson1D( v, L ):
    # Solve 1-d Poisson equation:
    #     d^u / dx^2 = v   for  0 <= x <= L
    # using spectral method
    J = len(v)
    # Fourier transform source term
    v_tilde = np.fft.fft(v)
    # vector of wave numbers
    k = (2*np.pi/L)*np.concatenate((np.linspace(0,J/2-1,J/2),np.linspace(-J/2,-1,J/2)))
    k[0] = 1
    # Calculate Fourier transform of u
    u_tilde = np.divide(-v_tilde,np.power(k,2))
    # Inverse Fourier transform to obtain u
    u = np.real(np.fft.ifft(u_tilde))
    # Specify arbitrary constant by forcing corner u = 0;
    u = u - u[0]
    return u

