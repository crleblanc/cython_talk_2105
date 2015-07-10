#include <stdint.h>
#include <stdio.h>

void ccumsum(const int64_t *input_array, int64_t *output_array, int64_t nelem) {
    int64_t sum = 0;
    int64_t idx;
    for (idx=0; idx<nelem; idx++) {
        sum += input_array[idx];
        output_array[idx] = sum;
    }
}