import numpy as np
cimport numpy as np
cimport cython
from cython.parallel import parallel, prange

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline void cy_update(np.ndarray[double, ndim=2] u, double dx2, double dy2):
    cdef int i, j
    for i in xrange(1,u.shape[0]-1):
        for j in xrange(1, u.shape[1]-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))


@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline void cy_update_parallel(np.ndarray[double, ndim=2] u, double dx2, double dy2):
    cdef int i, j

    for i in prange(1, u.shape[0]-1, nogil=True):
        for j in xrange(1, u.shape[1]-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))

def cy_run(np.ndarray[double, ndim=2] work_array, double dx2, double dy2, int niter):
    cdef int x
    for x in xrange(niter):
        cy_update(work_array, dx2, dy2)

def cy_run_parallel(np.ndarray[double, ndim=2] work_array, double dx2, double dy2, int niter):
    cdef int x
    for x in xrange(niter):
        cy_update_parallel(work_array, dx2, dy2)
