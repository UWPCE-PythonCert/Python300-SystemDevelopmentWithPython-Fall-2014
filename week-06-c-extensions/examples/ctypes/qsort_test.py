#!/usr/bin/env python

import ctypes

libc = ctypes.CDLL("libc.dylib")

TenInts = ctypes.c_int * 10
data = TenInts(*range(10,0,-1))

# http://www.gnu.org/software/libc/manual/html_node/Array-Sort-Function.html
# void qsort (void *array, size_t count, size_t size, comparison_fn_t compare)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def py_cmp_func(a, b):
    # print "py_cmp_func", a[0], b[0]
    return a[0] - b[0]

for i in data:
    print i

libc.qsort(data, len(data), ctypes.sizeof(ctypes.c_int), CMPFUNC(py_cmp_func))

for i in data:
    print i
