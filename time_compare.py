# ipython script to do timings on various 2D laplace implementations
from __future__ import print_function
import time
import numpy as np
from matplotlib import pyplot as plt
import py_laplace
import np_laplace
import cy_laplace
import cy_wrap_claplace
import numba_laplace # requires numba, easiest to use Anaconda distribution

laplace_funcs = (
                 ('pure Python', py_laplace.py_update),
                 ('Numpy', np_laplace.num_update),
                 ('Cython', cy_laplace.cy_update),
                 ('Cython C wrapper', cy_wrap_claplace.cy_update_c_wrap),
                 ('Cython parallel', cy_laplace.cy_update_parallel),
                 ('Numba laplace loops', numba_laplace.numba_update),
                 ('Numba laplace vectorized', numba_laplace.numba_update_vectorized),
                 )

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy


def run_all(plot_data=False, maxtime=50):
    results = []
    for name, laplace_func in laplace_funcs:

        niter = 10
        # don't make it bigger than 20000, that's a massive array!
        #array_shapes = [10, 20, 50, 100, 200, 500, 1000, 3000, 5000, 10000, 15000, 20000]
        array_shapes = [10, 20, 50, 100, 200, 500, 1000, 3000]

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

            time_diff = t2-t1
            times.append(time_diff)
            shapes.append(array_shape)
            print(name, array_shape, t2-t1)

            #%timeit laplace_func(work_array, dx2, dy2)

            if plot_data:
                plt.imshow(work_array)
                plt.show()

        results.append((name, shapes, times))
        print(name, shapes, times)

    return results


def plot_results(results):
    for name, niter, time in results:
        plt.plot(niter, time, label=name)

    plt.legend()
    #plt.title('Runtime vs. array size of 2D Laplace implementations')
    plt.xlabel('array size (x and y)')
    plt.ylabel('runtime (s)')
    plt.show()


def main():
    results = run_all(plot_data=False)
    plot_results(results)

if __name__ == '__main__':
    main()
