#!/usr/bin/env python
#
# Unit tests to make sure we're getting the same results across all implementations

import unittest
import numpy as np
import py_laplace
import np_laplace


class TestLaplaceImplementations(unittest.TestCase):

    def setUp(self):
        self.array_size = (100, 100)
        self.niter = 1000
        self.dx = 0.1
        self.dy = 0.1
        self.dx2 = self.dx*self.dx
        self.dy2 = self.dy*self.dy
        self.u = self.getStartingArray()
        self.reference_array = self.getNumpy()

    def getStartingArray(self):
        # set the state of the input array, the first row is all 1.0 and everywhere else is 0.0
        arr = np.zeros(self.array_size, dtype=np.float64)
        arr[0] = 1.0
        return arr

    def getNumpy(self):
        """return the array generated by the NumPy 2D Laplace implementation.  This is our reference implementation"""

        work_array = self.getStartingArray()
        for _ in range(self.niter):
            np_laplace.num_update(work_array, self.dx2, self.dy2)

        return work_array

    def runComparison(self, updater):
        for _ in range(self.niter):
            updater(self.u, self.dx2, self.dy2)

        # arrays can differ a lot but tend to converge at large N, see http://wiki.scipy.org/PerformancePython
        np.testing.assert_almost_equal(self.u, self.reference_array, decimal=1)
        # self.plotDifferences()

    def plotDifferences(self):
        """Plot the differences between the updated array and the reference.  Shouldn't be included in a normal unit test
        since it uses graphical displays"""
        from matplotlib import pyplot as plt

        plt.subplot(1, 3, 1)
        plt.imshow(self.u)
        plt.subplot(1, 3, 2)
        plt.imshow(self.reference_array)
        plt.subplot(1, 3, 3)
        plt.imshow(self.reference_array - self.u)
        plt.show()

    def testPython(self):
        self.runComparison(py_laplace.py_update)

    def testCython(self):
        import cy_laplace
        self.runComparison(cy_laplace.cy_update)

    def testCythonCWrap(self):
        import cy_wrap_claplace
        self.runComparison(cy_wrap_claplace.cy_update_c_wrap)

    def testCythonParallel(self):
        import cy_laplace
        self.runComparison(cy_laplace.cy_update_parallel)

    def testNumbaLooped(self):
        import numba_laplace # requires numba, easiest to use Anaconda distribution
        self.runComparison(numba_laplace.numba_update)

    def testNumbaVectorized(self):
        import numba_laplace
        self.runComparison(numba_laplace.numba_update_vectorized)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
