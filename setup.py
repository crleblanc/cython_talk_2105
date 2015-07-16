# Builds the Cython modules, good examples at https://github.com/cython/cython/tree/master/Demos
from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Build import cythonize
    USE_CYTHON=True
except ImportError:
    USE_CYTHON=False

extensions = [ Extension('cy_laplace',['cy_laplace.pyx'],
                         extra_compile_args=['-fopenmp'],
                         extra_link_args=['-fopenmp']
                         ),
               Extension('cy_wrap_claplace',['cy_wrap_claplace.pyx', 'claplace.c'],
                         extra_compile_args=['-fopenmp'],
                         extra_link_args=['-fopenmp']
                         ),
               # Extension('c_laplace_wrapper', ['c_laplace_wrapper.pyx', 'c_laplace.c'])
              ]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name = 'Demos',
    ext_modules = extensions,
    )