import numpy as np

def double_maxwellian(N,vb):
    v1 = np.random.normal(-1,vb,int(N/2))
    v2 = np.random.normal(1,vb, int(N/2))
    v = np.concatenate((v1, v2))

    return v
