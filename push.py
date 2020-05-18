


def timestep(r,v,N,J,dt,L):
    # load r,v into a single vector
    solution_coeffs = np.concatenate((r, v))

    # take a 4th order Runge-Kutta timestep
    k1 = AssembleRHS(solution_coeffs, L, J, N)
    k2 = AssembleRHS(solution_coeffs + 0.5 * dt * k1, L, J, N)
    k3 = AssembleRHS(solution_coeffs + 0.5 * dt * k2, L, J, N)
    k4 = AssembleRHS(solution_coeffs + dt * k3, L, J, N)
    solution_coeffs = solution_coeffs + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    # unload solution coefficients
    r = solution_coeffs[0:N]
    v = solution_coeffs[N:2 * N]
    # make sure all coordinates are in the range 0 to L
    r = r + L * (r < 0) - L * (r > L)
    return [r,v,k1,k2,k3,k4,solution_coeffs]