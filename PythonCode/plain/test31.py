#!/usr/bin/env python3
import numpy
import time
'''
 # shift() definition
 # simple_feature() definition
(    shift(X=X, shift_win=30)   - 2*  shift(X=X,shift_win=15) + X    ) < -1e-13 
? 1 : (shift(X=X, shift_win=1) - X)
'''
def shift(a:list[float],shift_win:int)->list[float]:
    l = len(a)
    if shift_win>=l:
        return [a[0] for i in range(l)]
    elif shift_win<=0:
        print("shift_win should be positive")
    else:
        return [a[0] for i in range(shift_win)] + a[:l-shift_win]

def simple_feature(a:list[float])->list[float]:
    filter = ( numpy.array(shift(a,30)) - 2.*numpy.array(shift(a,15)) + numpy.array(a) ) < -1e-13
    b = numpy.array(shift(a,1)) - numpy.array(a)
    return [1. if e else b[i] for i,e in enumerate(filter)]

def test():
     numpy.random.seed(1)
     tic = time.time()
     A = numpy.random.random(200000).astype(numpy.float64) * 300 - 160
     toc = time.time()
     print("Data generation time: {} ms.".format((toc - tic) * 1e3))
     tic = time.time()
     B = simple_feature(list(A))
     toc = time.time()
     print("Computing time: {} ms.".format((toc - tic) * 1e3))

if __name__ == "__main__":
    test()