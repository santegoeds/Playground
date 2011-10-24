#!/usr/bin/env python

from timeit import timeit

iterations  = 1000000
number = 1000

print "Python:", timeit(
    setup = "from monte_carlo.python import calc_pi",
    stmt = "calc_pi(%d)" % iterations,
    number = number 
)

print "Cython 1:", timeit(
    setup = "from monte_carlo.cython import calc_pi_1",
    stmt = "calc_pi_1(%d)" % iterations,
    number = number
)

print "Cython 2:", timeit(
    setup = "from monte_carlo.cython import calc_pi_2",
    stmt = "calc_pi_2(%d)" % iterations,
    number = number
)

print "Cython MT 1:", timeit(
    setup = "from monte_carlo.cython import calc_pi_3",
    stmt = "calc_pi_3(%d)" % iterations,
    number = number
)


