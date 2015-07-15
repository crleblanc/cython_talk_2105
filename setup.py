# Builds the Cython modules, good examples at https://github.com/cython/cython/tree/master/Demos
from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Build import cythonize
    USE_CYTHON=True
except ImportError:
    USE_CYTHON=False

extensions = [Extension('c_wrap_sin', ['c_wrap_sin.pyx', 'c_sin.c']),
              Extension('cy_sin.pyx',['cy_sin.pyx'])
              ]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name = 'Demos',
    ext_modules = extensions,
    )