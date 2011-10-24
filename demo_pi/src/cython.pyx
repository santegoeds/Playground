#
# Accessing a C library.
#
cdef extern from "stdlib.h":
    double drand48() nogil

def random():
    return drand48()


#
# Simple Cython
#
import math

def calc_pi_1(n):
    inside = 0

    for _ in range(n):
        x, y = drand48(), drand48()
        if math.sqrt(x**2 + y**2) <= 1.0:
            inside += 1

    return float(inside)/n * 4.0


#
# Optimised Cython
#
cdef extern from "math.h":
    double sqrt(double) nogil

cpdef double calc_pi_2(long n):
    cdef:
        double x, y
        long inside = 0

    for _ in range(n):
        x, y = drand48(), drand48()
        if sqrt(x**2 + y**2) < 1.0:
            inside += 1

    return <double>inside/n * 4.0


from cython.parallel import prange

cpdef double calc_pi_3(long n):
    cdef:
        double x, y
        long inside = 0
        long i

    for i in prange(n, nogil=True):
        x, y = drand48(), drand48()
        if sqrt(x**2 + y**2) < 1.0:
            inside += 1

    return <double>inside/n * 4.0

