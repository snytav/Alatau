from accum import accum
import numpy as np
def GetDensity( r, L, J ):
# Evaluate number density n in grid of J cells, length   L, from the electron positions r

    dx = L/J
    #return dx

    js = np.floor(r/dx)
    #return js
    ys = r/dx - (js)
    #js -= 1
    #return ys
    n1 =  ys

    j = np.mod(js,J) + 1
    j = j + J*(j<0) - J*(j>=J)
    js_plus_1 = j


    #return js_plus_1
    n1 = accum(js.astype(int),(1-ys)/dx)
    np.savetxt('n1.txt', n1, delimiter='\n',fmt='%15.5e')
    np.savetxt('js.txt', js+1,delimiter='\n',fmt='%15d')
    np.savetxt('js_plus_1.txt', js_plus_1+1, delimiter='\n',fmt='%15d')
    np.savetxt('ys_dx.txt', ys/dx, delimiter='\n',fmt='%15.5e')
    n2 = accum(js_plus_1.astype(int),ys/dx)
    np.savetxt('n2.txt', n2, delimiter='\n',fmt='%15.5e')
    n = n1 + n2

    return n
