#!/usr/bin/env python
# Running the Pypy laplace demo from a standalone script since 
# it cannot import Cython C extensions, matplotlib, etc.

import json
from run_comparison import run_all
import py_laplace

if __name__ == '__main__':
    array_shapes = [10, 12, 15, 18, 20, 35, 50, 100, 200, 500, 800, 1000, 1500, 2000, 3162]
    laplace_funcs = (('Pure Python (Pypy)', py_laplace.py_run),)
    
    pypy_results = run_all(laplace_funcs, array_shapes)
    
    with open('pypy_results.json', 'w') as fp:
        json.dump(pypy_results[0], fp)