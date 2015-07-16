# ipython script to do timings on various cumsum implementations
from __future__ import print_function
import time
import numpy as np
from matplotlib import pyplot as plt
import py_laplace
import np_laplace
import cy_laplace
import cy_wrap_claplace

laplace_funcs = (
                 #('pure Python', py_laplace.py_update),
                 ('Numpy', np_laplace.num_update),
                 ('Cython', cy_laplace.cy_update),
                 ('Cython C wrapper', cy_wrap_claplace.cy_update_c_wrap),
                 ('Cython parallel', cy_laplace.cy_update_parallel),
                 )

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy

def run_all(plot_data=False):
    results = []
    for name, laplace_func in laplace_funcs:

        niter = 10
        # don't make it bigger than 20000, that's a massive array!
        array_shapes = [10, 20, 50, 100, 200, 500, 1000, 5000, 10000, 15000, 20000]

        times = []
        for array_shape in array_shapes:
            work_array = np.zeros([array_shape, array_shape], dtype=np.float64)
            work_array[0] = 1.0

            t1 = time.time()
            for x in range(niter):
                laplace_func(work_array, dx2, dy2)
            t2 = time.time()

            times.append(t2-t1)
            print(name, array_shape, t2-t1)

            #%timeit laplace_func(work_array, dx2, dy2)

        results.append((name, array_shapes, times))
        #print(name, array_shapes, times)


        if plot_data:
            plt.imshow(work_array)
            plt.show()

    return results

def plot_results(results):
    print (results)
    for name, niter, time in results:
        plt.plot(niter, time, label=name)

    plt.legend()
    #plt.title('Contour plot of user-specified triangulation')
    plt.xlabel('array size (x and y)')
    plt.ylabel('runtime (s)')
    plt.show()

def main():
    results = run_all()
    plot_results(results)

if __name__ == '__main__':
    main()
