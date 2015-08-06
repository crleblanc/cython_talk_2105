#!/usr/bin/env python
# requires "# cython: profile=True" at the top of cy_laplace.pyx
import pstats, cProfile
import numpy as np
import cy_laplace

def myprofiler():
    niter = 20
    work_array = np.zeros((5000, 5000), dtype=np.float64)
    work_array[0] = 1
    for i in range(niter):
        cy_laplace.cy_update(work_array, 0.1, 0.1)

cProfile.runctx("myprofiler()", globals(), locals(), "profile.prof")

s = pstats.Stats("profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
