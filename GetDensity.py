from accum import accum
import numpy as np
from internal_element_wise import internal_element_wise_multiply

def GetDensity( r, L, J ):
# Evaluate number density n in grid of J cells, length   L, from the electron positions r

    dx = np.divide(L,J)
    #return dx

    js = np.floor(np.divide(r,dx))
    #return js
    ys = np.divide(r,dx) - (js)
    #js -= 1
    #return ys
    n1 =  ys

    j = np.mod(js,J) + 1
    j = j + J*(j<0) - J*(j>=J)
    js_plus_1 = j


    #return js_plus_1
    accmap = js.astype(int)
    a = np.divide((1-ys),dx)
    n1 = accum(accmap,a) #js.astype(int),np.divide((1-ys),dx))
    n11 = internal_element_wise_multiply(n1)


    np.savetxt('n1.txt', n1, delimiter='\n',fmt='%15.5e')
    np.savetxt('js.txt', js+1,delimiter='\n',fmt='%15d')
    np.savetxt('js_plus_1.txt', js_plus_1+1, delimiter='\n',fmt='%15d')
    np.savetxt('ys_dx.txt', ys/dx, delimiter='\n',fmt='%15.5e')
    n2 = accum(js_plus_1.astype(int),np.divide(ys,dx))
    np.savetxt('n2.txt', n2, delimiter='\n',fmt='%15.5e')
    n = n1 + n2

    return n
