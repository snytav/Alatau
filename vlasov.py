import matplotlib.pyplot as plt
import numpy as np


def spectral_field(dens):
    Nx = len(dens)
    rho = np.fft.fft(1 - dens)
    k_in = 0.5;  # smallest non-zero k (k-resolution)
    Lx = 2 * np.pi / k_in
    kx_ind = np.linspace(1, Nx, Nx) - Nx / 2 - 1
    kx = 2 * np.pi / Lx * kx_ind  # kx-vector

    E = np.divide(np.fft.fftshift(rho), 1j * kx)
    E[int(Nx / 2)] = 0
    E = np.fft.ifft(np.fft.fftshift(E))
    return E


dens = np.loadtxt('dens_3.txt', delimiter='\n', unpack=True)
E = spectral_ield(dens)
