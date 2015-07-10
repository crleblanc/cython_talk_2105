# wrap a C cumsum implementation written in C
import numpy as np
cimport numpy as np
cimport cython
# Some necessary C integer types instead of using "long long", int64_t == np.int64_t
from libc.stdint cimport int64_t

# C function declaration
cdef extern from "cumsum.h":
    void ccumsum(const int64_t *input_array, int64_t *output_array, int64_t nelem)

def cumsum_c_wrap(np.ndarray[np.int64_t, ndim=1] input_array):
    cdef:
        np.ndarray[np.int64_t, ndim=1] output_array = np.empty_like(input_array)
        np.int64_t nelem = input_array.shape[0]
        int64_t *input_array_ptr
        int64_t *output_array_ptr

    input_array_ptr = &input_array[0]
    output_array_ptr = &output_array[0]

    ccumsum(input_array_ptr, output_array_ptr, nelem)

    return output_array