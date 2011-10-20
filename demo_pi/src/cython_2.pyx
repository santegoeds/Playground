from libc.math cimport sqrt
from libc.stdlib cimport rand, RAND_MAX

cdef double random():
    return <double>rand() / (<double>RAND_MAX + 1)

cpdef double calc_pi(int n):
    cdef:
        int inside = 0, i = 0
        double pi, x, y

    while i < n:
        i += 1
        x = random()
        y = random()
        if sqrt(x**2 + y**2) <= 1:
            inside += 1
    pi = 4.0 * inside / i
    return pi

