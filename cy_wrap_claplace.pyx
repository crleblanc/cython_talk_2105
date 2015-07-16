import numpy as np
cimport numpy as np
cimport cython
from libc.stdint cimport int64_t

cdef extern from "claplace.h":
    void c_update(double *u, int x_len, int y_len, double dx2, double dy2)

def cy_update_c_wrap(np.ndarray[double, ndim=2] u, dx2, dy2):
    """Wrap a C function that performs the 2D Laplace equation in-place"""

    c_update(<double *> &u[0,0], u.shape[0], u.shape[1], dx2, dy2)
