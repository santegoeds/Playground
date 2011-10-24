from .cython import random, calc_pi_2
from math import sqrt

def calc_pi(n):
    inside = 0
    for _ in range(n):
        x, y = random(), random()
        if sqrt(x**2 + y**2) <= 1.0:
            inside += 1
    return float(inside)/n * 4.0


import multiprocessing as mp

def mthread_pi(n):
    thr_cnt = mp.cpu_count() * 2
    pool = mp.pool.ThreadPool(thr_count)
    result = pool.map_async(calc_pi_2, [n / 100 ] * 100)
    return avg(result.get())

