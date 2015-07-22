# cython_talk_2105

Demo code for my Kiwi Pycon talk on Cython.  Build all Cython modules using this command:
"python setup.py build_ext --inplace --force".  These have been build using gcc on Ubuntu
14.04, so may need some tweaking on Windows or Mac, but not much.

Run the benchmarks by running "python time_compare.py".  If running the Numba example,
you'll need Numba installed.  The easiest way to do this is to use the free Anaconda
Python distribution.

This presentation will try some new approaches that were not available when these two posts
were written: http://wiki.scipy.org/PerformancePython,
http://technicaldiscovery.blogspot.co.nz/2011/06/speeding-up-python-numpy-cython-and.html.
