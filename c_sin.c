#include <stdint.h>
#include <math.h>
#include <stdio.h>

void c_sin(const double *input_array, double *output_array, int64_t nelem) {
    int64_t idx;
    for (idx=0; idx<nelem; idx++) {
        output_array[idx] = sin(input_array[idx]);
    }
}
