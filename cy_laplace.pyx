cimport numpy as np
cimport cython
from cython.parallel import parallel, prange

@cython.boundscheck(False)
@cython.wraparound(False)
def cy_update(np.ndarray[double, ndim=2] u, double dx2, double dy2):
    cdef int i, j
    for i in xrange(1,u.shape[0]-1):
        for j in xrange(1, u.shape[1]-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))


# These buy us a 2X speedup for big arrays!
@cython.boundscheck(False)
@cython.wraparound(False)
def cy_update_parallel(np.ndarray[double, ndim=2] u, double dx2, double dy2):
    cdef int i, j

    # according to http://cs.anu.edu.au/~Alistair.Rendell/papers/wompei2005.pdf, we should
    # place a paralle() before this loop.  Hmm, experiment.  Our approach works well with large arrays

    #with nogil, parallel():
    for i in prange(1, u.shape[0]-1, nogil=True):
        for j in xrange(1, u.shape[1]-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))
