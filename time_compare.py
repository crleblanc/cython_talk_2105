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

laplace_funcs = (#('pure Python', py_laplace.py_update),
                 #('Numpy', np_laplace.num_update),
                 ('Cython', cy_laplace.cy_update),
                 ('Cython C wrapper', cy_wrap_claplace.cy_update_c_wrap),
                 ('Cython parallel', cy_laplace.cy_update_parallel),
                 #('Numba laplace vectorized', numba_laplace.numba_update_vectorized),
                 #('Numba laplace loops', numba_laplace.numba_update),
                 )

niter = 10
dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy


def filtered_mean(runtimes, n_mean=3):
    """Returns the mean of the top n times in the input sequence, discarding the slowest times if more than three available"""

    sorted_times = sorted(runtimes)

    if len(sorted_times) > n_mean:
        sorted_times = sorted_times[0:n_mean]

    return np.mean(sorted_times)


def run_all(plot_data=False, maxtime=25):
    results = []
    for name, laplace_func in laplace_funcs:

        # don't make it bigger than 20000, that's a massive array!
        #array_shapes = [5, 6, 8, 10, 12, 15, 20, 50, 100, 200, 500, 1000, 5000, 10000, 15000]
        #array_shapes = [20, 50, 100, 200, 400, 500, 1000, 1500, 2000]
        array_shapes = [500, 1000, 15000]

        time_diff = 0
        times = []
        sizes = []
        for array_shape in array_shapes:
            if time_diff > maxtime:
                continue

            work_array = np.zeros([array_shape, array_shape], dtype=np.float64)
            work_array[0] = 1.0

            runtimes = []
            for x in range(niter):
                t1 = time.time()
                laplace_func(work_array, dx2, dy2)
                t2 = time.time()
                runtimes.append(t2-t1)

            times.append(filtered_mean(runtimes))
            sizes.append(work_array.size)
            print(name, array_shape, '%0.3f' % min(runtimes))

            if plot_data:
                plt.imshow(work_array)
                plt.show()

        results.append((name, sizes, times))

    return results


def plot_results(results):

    plt.subplot(2, 1, 1)
    for name, iter_count, time in results:
        plt.plot(iter_count, time, '.-', label=name)
    #plt.ylim(0, 4)
    plt.legend(loc=2)
    plt.title('2D Laplace Python implementation benchmark (iterations=%d)' % niter)
    plt.xlabel('array size (X*Y)')
    plt.ylabel('time per iteration (s)')

    plt.subplot(2, 1, 2)
    for name, iter_count, time in results:
        plt.loglog(iter_count, time, '.-', label=name)
    plt.legend(loc=2)
    plt.xlabel('array size (X*Y)')
    plt.ylabel('time per iteration (s)')

    plt.show()


def main():
    results = run_all(plot_data=False)
    plot_results(results)

if __name__ == '__main__':
    main()
