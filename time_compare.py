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
from run_comparison import run_all

def getargs():
    parser = argparse.ArgumentParser(description='Time and/or plot the timings of the Laplace benchmarks')
    parser.add_argument('-t', '--timing', dest='timing', action='store_true',
                    help='Run the timing operation')
    parser.add_argument('-p', '--plot', dest='plot', action='store_true',
                    help='Plot the data from results.json obtained from an earlier run, see --timing')

    return parser.parse_args()


def plot_results(results_list, xmin, xmax, ymin, ymax):
    matplotlib.rcParams.update({'font.size': 22})
    plt.figure(figsize=(8,11), tight_layout=True)
    plt.title('2D Laplace Python implementation benchmark')
    
    results, pypy_results = results_list
    # place Pypy result as the second graph.  Results run from 'run_pypy_laplce.py' using pypy/numpypy.
    results.insert(1, pypy_results)
    
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
    # don't make it bigger than 20000, that's a massive array!
    #array_shapes = [10, 20, 50, 100, 200, 500, 1000, 3000, 5000, 10000, 15000, 20000]
    array_shapes = [10, 12, 15, 18, 20, 35, 50, 100, 200, 500, 800, 1000, 1500, 2000, 3162]
    ymax = array_shapes[-1]/25000.0

    results = None
    pypy_results = None
    args = getargs()
    
    laplace_funcs = (('Pure Python (Cpython)', py_laplace.py_run),
                    ('NumPy', np_laplace.np_run),
                    ('Numba', numba_laplace.numba_run),
                    ('Cython', cy_laplace.cy_run),
                    ('Cython C wrapper', cy_wrap_claplace.cy_run_c_wrap),
                    ('Cython parallel', cy_laplace.cy_run_parallel),
                    # ('Numba laplace vectorized', numba_laplace.numba_run_vectorized),
                    )

    if args.timing:
        results = run_all(laplace_funcs, array_shapes, maxtime=ymax)
        
        with open('results.json', 'w') as fp:
            json.dump(results, fp)

    if args.plot:
        if results is None:
            with open('results.json', 'r') as fp:
                results = json.load(fp)
            
            with open('pypy_results.json', 'r') as pypy_fp:
                pypy_results = json.load(pypy_fp)

        plot_results([results, pypy_results], array_shapes[0]**2, array_shapes[-1]**2, 10e-8, ymax)


if __name__ == '__main__':
    main()
