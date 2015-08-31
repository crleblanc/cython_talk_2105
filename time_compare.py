#!/usr/bin/env python
# python script to do timings on various 2D laplace implementations
from __future__ import print_function
import time
import argparse
import numpy as np
import json
import matplotlib
from matplotlib import pyplot as plt
import py_laplace
import np_laplace
import cy_laplace
import cy_wrap_claplace
import numba_laplace # requires numba, easiest to use Anaconda distribution

laplace_funcs = (('Pure Python', py_laplace.py_run),
                 ('NumPy', np_laplace.np_run),
                 ('Numba', numba_laplace.numba_run),
                 ('Cython', cy_laplace.cy_run),
                 ('Cython C wrapper', cy_wrap_claplace.cy_run_c_wrap),
                 ('Cython parallel', cy_laplace.cy_run_parallel),
                 # ('Numba laplace vectorized', numba_laplace.numba_run_vectorized),
                )

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy

def getargs():
    parser = argparse.ArgumentParser(description='Time and/or plot the timings of the Laplace benchmarks')
    parser.add_argument('-t', '--timing', dest='timing', action='store_true',
                    help='Run the timing operation')
    parser.add_argument('-p', '--plot', dest='plot', action='store_true',
                    help='Plot the data from results.json obtained from an earlier run, see --timing')

    return parser.parse_args()


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

            #t1 = time.time()
            #for x in xrange(niter):
                #laplace_func(work_array, dx2, dy2)
            #t2 = time.time()
            t1 = time.time()
            laplace_func(work_array, dx2, dy2, niter)
            t2 = time.time()

            time_diff = (t2-t1)/niter
            times.append(time_diff)
            shapes.append(work_array.size)
            print(name, array_shape, time_diff)

            if plot_data:
                plt.imshow(work_array)
                plt.show()

        results.append({'name':name, 'array_shapes':shapes, 'times':times})
        print(name, shapes, times)

    return results


def plot_results(results, xmin, xmax, ymin, ymax):
    matplotlib.rcParams.update({'font.size': 22})
    plt.figure(figsize=(8,11), tight_layout=True)
    plt.title('2D Laplace Python implementation benchmark')
    for idx, result in enumerate(results):
        name = result['name']
        array_shapes = result['array_shapes']
        times = result['times']

        plt.subplot(2, 1, 1)
        plt.xlabel('array size (X*Y)')
        plt.ylabel('time per iteration (s)')
        plt.xlim(0, xmax)
        plt.ylim(0, ymax)
        plt.plot(array_shapes, times, '.-', linewidth=2.0, label=name)
        legend = plt.legend(loc='upper right', bbox_to_anchor=(1.9, 1.0), framealpha=0.0)

        plt.subplot(2, 1, 2)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel('array size (X*Y)')
        plt.ylabel('time per iteration (s)')
        plt.loglog(array_shapes, times, '.-', linewidth=2.0, label=name)

        plt.savefig('slides/results-%d.svg' % idx,
                    bbox_extra_artists=(legend,),
                    bbox_inches='tight',
                    transparent=True)

    #plt.show()


def main():
    niter=100
    # don't make it bigger than 20000, that's a massive array!
    #array_shapes = [10, 20, 50, 100, 200, 500, 1000, 3000, 5000, 10000, 15000, 20000]
    array_shapes = [10, 12, 15, 18, 20, 35, 50, 100, 200, 500, 800, 1000, 1500, 2000, 3162]
    ymax = array_shapes[-1]/25000.0

    results = None
    args = getargs()

    if args.timing:
        results = run_all(array_shapes, niter=niter, maxtime=ymax, plot_data=False)
        
        with open('results.json', 'w') as fp:
            json.dump(results, fp)

    if args.plot:
        if results is None:
            with open('results.json', 'r') as fp:
                results = json.load(fp)

        plot_results(results, array_shapes[0]**2, array_shapes[-1]**2, 10e-8, ymax)


if __name__ == '__main__':
    main()
