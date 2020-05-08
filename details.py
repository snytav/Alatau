import numpy as np

def detailed_output(t,dt,solution_coeffs,k1,k2,k3,k4):
    basefn = str(t)+ '.txt'
    solcoef_fn = 'solcoef_'+  basefn
    np.savetxt(solcoef_fn, solution_coeffs, delimiter='\n', fmt='%25.15e')
    if t < 10 * dt:
       fname = 'k1_' + str(t) + '.txt'
       np.savetxt(fname, k1, delimiter='\n', fmt='%25.15e')
       fname = 'k2_' + str(t) + '.txt'
       np.savetxt(fname, k2, delimiter='\n', fmt='%25.15e')
       fname = 'k3_' + str(t) + '.txt'
       np.savetxt(fname, k3, delimiter='\n', fmt='%25.15e')
       fname = 'k4_' + str(t) + '.txt'
       np.savetxt(fname, k4, delimiter='\n', fmt='%25.15e')