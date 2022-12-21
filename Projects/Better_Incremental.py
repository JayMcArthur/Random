from operator import  add
import math as m
import time


def layer_test():
    # Better way to calculate offline tiered adders (A add to B, B adds to C, C makes money)
    ##### Var Setup
    # Highest on left
    layers = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] + [0]*60
    # how much of the lower tier is created, so L[0] creates P[0] of L[1]
    # This basically shows any bonus could be included in this type of setup
    production = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] + [1]*60
    # Just holds the output for my method
    temp = [0] * len(layers)
    # we need to read what we started with so this gets ready for that
    test = layers + [0]
    # Amount of time to pass
    steps = 100 * 60 * 60 * 24

    ##### Functions
    # My Math Method
    s_t1 = time.time()
    for i in range(len(layers)):
        for j in range(i, len(layers)):
            temp[j] += m.comb(steps, j - i + 1) * m.prod(production[i:(j + 1)]) * layers[i]
    f_t1 = time.time() - s_t1
    temp = [0] + temp
    layers = layers + [0]
    temp = list(map(add, temp, layers))
    print("--- {0} seconds --- {1}".format(f_t1, temp))

    # Emulation of Time Passing
    s_t2 = time.time()
    for i in range(steps):
        for j in range(len(test)-2, -1, -1):
            test[j+1] += test[j] * production[j]
    f_t2 = time.time() - s_t2
    print("--- {0} seconds --- {1}".format(f_t2, test))
    # Copyright 2021, Jay McArthur, All rights reserved.
