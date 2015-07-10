# importing numpy but not using any of it's features
import numpy as np


def cumsum(input_array):
    """ultra simple cumsum implementation in pure Python"""
    output_array = np.empty_like(input_array)
    sum = 0
    for idx, in_element in enumerate(input_array):
        sum += in_element
        output_array[idx] = sum

    return output_array