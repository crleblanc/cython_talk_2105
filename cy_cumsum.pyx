import numpy as np
cimport numpy as np
cimport cython

def cumsum_slow(input_array):
    """ultra simple cumsum implementation in pure Python"""
    sum = 0
    for element in input_array:
        sum += element
    return sum

def cumsum(np.ndarray[np.int64_t, ndim=1] input_array):
    cdef:
        np.int64_t sum=0
        np.int64_t element
        np.ndarray[np.int64_t, ndim=1] output_array = np.empty_like(input_array)

    for idx in range(input_array.shape[0]):
        sum += input_array[idx]
        output_array[idx] = sum

    return output_array

#@cython.boundscheck(False)
#@cython.wraparound(False)
#@cython.nonecheck(False)
def cumsum_memview(np.ndarray[np.int64_t, ndim=1] input_array):
    cdef:
        np.int64_t sum=0
        np.int64_t idx
        np.int64_t[:] array_view = input_array
        np.ndarray[np.int64_t, ndim=1] output_array = np.empty_like(input_array)

    for idx in range(input_array.shape[0]):
        sum += input_array[idx]
        output_array[idx] = sum

    return output_array