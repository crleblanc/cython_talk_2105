# wrap a C sin implementation written in C
import numpy as np
cimport numpy as np
cimport cython
from libc.stdint cimport int64_t

# C function declaration
cdef extern from "c_sin.h":
    void c_sin(const double *input_array, double *output_array, int64_t nelem)

def c_wrapper(np.ndarray[np.float64_t, ndim=1] input_array):
    cdef:
        np.ndarray[np.float64_t, ndim=1] output_array = np.empty_like(input_array)
        np.int64_t nelem = input_array.shape[0]
        np.float64_t *input_array_ptr
        np.float64_t *output_array_ptr

    input_array_ptr = &input_array[0]
    output_array_ptr = &output_array[0]

    c_sin(input_array_ptr, output_array_ptr, nelem)

    return output_array

def dummy(np.ndarray[np.float64_t, ndim=1] input_array):
    """Dummy function to determine the overhead without the algorithm"""
    cdef:
        np.ndarray[np.float64_t, ndim=1] output_array = np.empty_like(input_array)
        np.int64_t nelem = input_array.shape[0]
        np.float64_t *input_array_ptr
        np.float64_t *output_array_ptr

    input_array_ptr = &input_array[0]
    output_array_ptr = &output_array[0]

    return output_array