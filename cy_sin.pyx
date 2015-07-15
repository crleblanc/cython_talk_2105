from __future__ import print_function
import numpy as np
import math
cimport numpy as np
cimport cython
# Fast C version of sin:
from libc.math cimport sin as libc_sin
cimport cython.parallel
cimport openmp
from cython.parallel import parallel, prange, threadid

def cython_sin_slow(input_array):
    """ultra simple sin implementation in pure Python"""
    output_list = []
    for element in input_array:
        output_list.append(math.sin(element))
    return np.array(output_list)




def cython_sin(np.ndarray[np.float64_t, ndim=1] input_array):
    cdef:
        np.int64_t idx
        np.ndarray[np.float64_t, ndim=1] output_array = np.empty_like(input_array)

    for idx in range(input_array.shape[0]):
        output_array[idx] = libc_sin(input_array[idx])

    return output_array




@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def cython_sin_memview(np.ndarray[np.float64_t, ndim=1] input_array):
    cdef:
        np.int64_t idx
        np.float64_t[:] array_view = input_array
        np.ndarray[np.float64_t, ndim=1] output_array = np.empty_like(input_array)

    for idx in range(input_array.shape[0]):
        output_array[idx] = libc_sin(input_array[idx])

    return output_array




def cython_sin_parallel(np.ndarray[np.float64_t, ndim=1] input_array):
    cdef:
        np.int64_t idx
        np.ndarray[np.float64_t, ndim=1] output_array = np.empty_like(input_array)

    for idx in prange(input_array.shape[0], nogil=True):
        output_array[idx] = libc_sin(input_array[idx])

    return output_array