import matplotlib.pyplot as plt
import math

def phase_space(t,dt,r,v):
    if math.floor(t / dt) % math.floor(5 / dt) == 0:
       plt.figure()
       plt.scatter(r,v,s=1)
       plt.xlabel('X')
       plt.ylabel('Y')
       tit = 'Electron Phase-space distribution for t = ' + str(t)
       plt.title(tit)
       plt.show()