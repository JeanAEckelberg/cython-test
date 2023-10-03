#!python
#cython: language_level=3, boundscheck=False

def add(int a, int b):
    cdef int result
    result = a + b
    return  result

