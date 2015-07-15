# importing numpy but not using any of it's features
import math
import numpy as np

def sin(input_array):
    """ultra simple sin implementation for an arry or list in pure Python.
    Returns a list"""
    return [math.sin(x) for x in input_array]
