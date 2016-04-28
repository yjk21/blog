from numpy import *
import time

def sigmoid(v):
    return 1.0 / (1.0 + exp(-v))

def step(xt, htm1, Wh, Wi):
    return sigmoid(dot(Wh, htm1) + Wi[xt,:])

def pyfwd(x,h0, Wh, Wi):
    ht = h0
    tic = time.time()
    for xt in x:
        ht = step(xt, ht, Wh,Wi)
    toc = time.time() - tic
    return ht, toc
