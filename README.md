# cython_talk_2105

Demo code for my Kiwi Pycon talk on Cython.  Build all Cython modules using this command:
"python setup.py build_ext --inplace --force".  These have been build using gcc on Ubuntu
14.04, so may need some tweaking on Windows or Mac.

Run the benchmarks by running "python time_compare.py".  If running the Numba example,
you'll need Numba installed.  The easiest way to do this is to use the free Anaconda
Python distribution.
