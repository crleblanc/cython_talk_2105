# NumPy version of 2D laplace equation from http://technicaldiscovery.blogspot.co.nz/2011/06/speeding-up-python-numpy-cython-and.html

import numpy as np

def num_update(u, dx2, dy2):
    u[1:-1,1:-1] = ((u[2:,1:-1] + u[:-2,1:-1])*dy2 +
                    (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))

def np_run(work_array, dx2, dy2, niter):
    for x in xrange(niter):
        num_update(work_array, dx2, dy2)
