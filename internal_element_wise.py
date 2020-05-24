import numpy as np

def internal_element_wise_multiply(a):
    if len(a.shape) == 1:
        return a

    res = np.ones(a.shape[0])

    for x in a.T:
        res = np.multiply(res,x)

    return res

