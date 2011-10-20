
from random import random
from math import sqrt

def calc_pi(n):
    inside = 0
    i = 0

    while i < 10000000:
        i += 1
        x = random()
        y = random()
        if sqrt(x**2 + y**2) <= 1:
            inside += 1
    pi = 4.0 * inside/i
    return pi

