# NumPy/Numba version of 2D laplace equation from http://technicaldiscovery.blogspot.co.nz/2011/06/speeding-up-python-numpy-cython-and.html
# requires Numba.  On Ubuntu: Ha!  Not easy, still working on it...
import numpy as np

def numba_update(u, dx2, dy2):
    u[1:-1,1:-1] = ((u[2:,1:-1]+u[:-2,1:-1])*dy2 +
                    (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))