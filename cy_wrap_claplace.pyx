import numpy as np
cimport numpy as np

cdef extern from "claplace.h":
    void c_update(double *u, int x_len, int y_len, double dx2, double dy2)

def cy_run_c_wrap(np.ndarray[double, ndim=2] u, double dx2, double dy2, int niter):
    cdef int x
    for x in xrange(niter):
        c_update(<double *> &u[0,0], u.shape[0], u.shape[1], dx2, dy2)
