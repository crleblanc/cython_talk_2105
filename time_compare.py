#!/usr/bin/env python
# python script to do timings on various 2D laplace implementations
from __future__ import print_function
import time
import numpy as np
from matplotlib import pyplot as plt
import py_laplace
import np_laplace
import cy_laplace
import cy_wrap_claplace
import numba_laplace # requires numba, easiest to use Anaconda distribution

laplace_funcs = (('pure Python', py_laplace.py_update),
                 ('Numpy', np_laplace.num_update),
                 ('Cython', cy_laplace.cy_update),
                 ('Cython C wrapper', cy_wrap_claplace.cy_update_c_wrap),
                 ('Cython parallel', cy_laplace.cy_update_parallel),
                 ('Numba laplace loops', numba_laplace.numba_update),
                 # ('Numba laplace vectorized', numba_laplace.numba_update_vectorized),
                )

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy


def run_all(array_shapes, niter=10, maxtime=25, plot_data=False):
    results = []
    for name, laplace_func in laplace_funcs:

        time_diff = 0
        times = []
        shapes = []
        for array_shape in array_shapes:
            if time_diff > maxtime:
                continue

            work_array = np.zeros([array_shape, array_shape], dtype=np.float64)
            work_array[0] = 1.0

            t1 = time.time()
            for x in range(niter):
                laplace_func(work_array, dx2, dy2)
            t2 = time.time()

            time_diff = (t2-t1)/niter
            times.append(time_diff)
            shapes.append(work_array.size)
            print(name, array_shape, time_diff)

            if plot_data:
                plt.imshow(work_array)
                plt.show()

        results.append((name, shapes, times))
        print(name, shapes, times)

    return results


def plot_results(results, xmin, xmax, ymin, ymax):
    plt.figure(figsize=(10,5))
    plt.title('2D Laplace Python implementation benchmark')
    for idx, (name, array_shape, time) in enumerate(results):
        plt.subplot(1, 2, 1)
        plt.xlabel('array size (X*Y)')
        plt.ylabel('time per iteration (s)')
        plt.xlim(0, xmax)
        plt.ylim(0, ymax)
        plt.plot(array_shape, time, '.-', label=name)
        plt.legend(loc=2, bbox_to_anchor=(0.05, 1), framealpha=0.0)

        plt.subplot(1, 2, 2)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel('array size (X*Y)')
        plt.ylabel('time per iteration (s)')
        plt.loglog(array_shape, time, '.-', label=name)
        #plt.legend(loc=2, bbox_to_anchor=(0.05, 1), framealpha=0.0)

        plt.savefig('slides/results-%d.png' % idx, transparent=True)
        plt.savefig('slides/results-%d.svg' % idx, transparent=True)

    plt.show()


def main():
    niter=100
    # don't make it bigger than 20000, that's a massive array!
    #array_shapes = [10, 20, 50, 100, 200, 500, 1000, 3000, 5000, 10000, 15000, 20000]
    array_shapes = [10, 12, 15, 18, 20, 35, 50, 100, 200, 500, 800, 1000, 1500, 2000, 3162]
    ymax = array_shapes[-1]/25000.0

    results = run_all(array_shapes, niter=niter, maxtime=ymax, plot_data=False)
    plot_results(results, array_shapes[0]**2, array_shapes[-1]**2, 10e-7, ymax)

if __name__ == '__main__':
    main()
