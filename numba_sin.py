# no point.  We need a better algorithm...
@
def numba_sin( input_array):
    output_array = np.empty_like(input_array)

    for idx in range(input_array.shape[0]):
        output_array[idx] = (input_array[idx])

    return output_array