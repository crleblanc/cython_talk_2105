Cython Intro: get the benefits of C without leaving Python.
###########################################################

.. Create a pdf of these slides with the command: rst2pdf -e inkscape -b1 -s slides.style slides.rst
.. Create an S5 html slide output with the command: rst2s5 slides.rst -d slides.html
.. TODO: get a nice image for the cover page, some svg for all backgrounds

Myself
------

* Background in Earth Sciences, Geophysics
* Using Python since 2001
* Software developer for GNS Science

.. TODO: background on Claritas.  Me: OBSs and seismics in Canada before coming to NZ to work on Claritas.

What is Cython
--------------

.. TODO: history of Cython, esp Greg Ewing from Uni of Canterbury!

* Creates a Python C extension from Cython code
* Can vastly improve performance vs Python
* Bridge from Python -> C
* Cython functions callable from C

Python vs. C example
--------------------

Python implementation
from https://docs.python.org/2/c-api/intro.html:

.. code-block:: python

    def incr_item(dict, key):
        try:
            item = dict[key]
        except KeyError:
            item = 0
        dict[key] = item + 1

.. raw:: pdf

   PageBreak

C equivalent:

.. code-block:: c
    
    int 
    incr_item(PyObject *dict, PyObject *key)
    {
        /* Objects all initialized to NULL for Py_XDECREF */
        PyObject *item = NULL,
        *const_one = NULL,
        *incremented_item = NULL;
        /* Return value initialized to -1 (failure) */
        int rv = -1;

        item = PyObject_GetItem(dict, key);
        if (item == NULL) {
            /* Handle KeyError only: */
            if (!PyErr_ExceptionMatches(PyExc_KeyError))
                goto error;

            /* Clear the error and use zero: */
            PyErr_Clear();
            item = PyInt_FromLong(0L);
            if (item == NULL)
                goto error;
        }
        const_one = PyInt_FromLong(1L);
        if (const_one == NULL)
            goto error;

        incremented_item = PyNumber_Add(item, const_one);
        if (incremented_item == NULL)
            goto error;

        if (PyObject_SetItem(dict, key, incremented_item) < 0)
            goto error;
        rv = 0; /* Success */
        /* Continue with cleanup code */

    error:
        /* Cleanup code, shared by success and failure path */

        /* Use Py_XDECREF() to ignore NULL references */
        Py_XDECREF(item);
        Py_XDECREF(const_one);
        Py_XDECREF(incremented_item);

        return rv; /* -1 for error, 0 for success */
    }

Cython Advantages
-----------------

* 99% Python
* Python 2/3 compatibility
* Classes
* Garbage collection
* Easy string handling
* Automatic reference counting
* Compliant C code: gcc, MSVC, etc.
* Stable, mature

Python demo counter
-------------------

.. code-block:: python

    def counter(count):
        x = 0
        for i in range(count):
            x += i

Cython demo counter
-------------------

.. code-block:: cython

    def counter(count):
        cdef int x = 0 # <- a C style data type
        for i in range(count):
            x += i

Cython demo counter
-------------------

.. code-block:: cython

    cdef int counter(int count):
        cdef int x = 0
        for i in range(count):
            x += i
        return x

.. TODO: cdeff-ed functions, cdeffed input args, numpy arrays (ok, later)

Cython and the GIL
------------------

GIL: Global Interpreter Lock

.. TODO: an image, something running one at a time instead of parallel.  TSA airport security!

Bypassing the GIL with C
------------------------

Modules that release the GIL:

* time.sleep()
* NumPy
* most C extensions

Cython nogil
------------

.. code-block:: cython

    def cython_func():
        with nogil:
            do_something()

Benchmarks
----------

.. TODO: add more!

.. image:: ../results-5.png
    :width: 100%


Caveats
-------

* Must re-acquire when using Python objects

.. TODO: show the PyQt demo, one with the GIL released, the other with it locked



.. footer::

    Get the benefits of C without leaving Python