import matplotlib.pyplot as plt
import math
import numpy as np

def phase_space(t,dt,r,v):
    if math.floor(t / dt) % math.floor(5 / dt) == 0:
       plt.figure()
       plt.scatter(r,v,s=1)
       plt.xlabel('X')
       plt.ylabel('Y')
       tit = 'Electron Phase-space distribution for t = ' + str(t)
       fname = 'phase-space_'+str(math.floor(t / dt))
       plt_fname = fname+'.png'
       plt.savefig(plt_fname)
       np.savetxt(fname, np.concatenate((r,v)) , fmt='%15.5e')
       plt.title(tit)
       #plt.show()
