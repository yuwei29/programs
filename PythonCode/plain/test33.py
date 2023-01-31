#!/usr/bin/env python3
import numpy
import time
'''
此版本 取 shift(X,shift_win)和simple_feature(X) 中的 X 均为 numpy array 
 # shift() definition
 # simple_feature() definition
(    shift(X=X, shift_win=30)   - 2*  shift(X=X,shift_win=15) + X    ) < -1e-13 
? 1 : (shift(X=X, shift_win=1) - X)
'''
def shiftL(a:list[float],shift_win:int)->list[float]:
    l = len(a)
    if shift_win>=l:
        return [a[0] for i in range(l)]
    elif shift_win<=0:
        print("shift_win should be positive")
    else:
        return [a[0] for i in range(shift_win)] + a[:l-shift_win]

def simple_featureL(a:list[float])->list[float]:
    filter = ( numpy.array(shiftL(a,30)) - 2.*numpy.array(shiftL(a,15)) + numpy.array(a) ) < -1e-13
    b = numpy.array(shiftL(a,1)) - numpy.array(a)
    return [1. if e else b[i] for i,e in enumerate(filter)]

def shift(a,shift_win:int):
    l = len(a)
    b = a[0]*numpy.ones_like(a)
    if shift_win>=l:
        return b
    elif shift_win<=0:
        print("shift_win should be positive")
    else:
        b[shift_win:] = a[:l-shift_win]
        return b

def simple_feature(a):
    filter = ( shift(a,30) - 2.*shift(a,15) + a ) < -1e-13
    b = shift(a,1) - a
    return numpy.where(filter,numpy.ones_like(a),b)

def test():
     numpy.random.seed(1)
     tic = time.time()
     A = numpy.random.random(200000).astype(numpy.float64) * 300 - 160
     toc = time.time()
     print("Data generation time: {} ms.".format((toc - tic) * 1e3))
     tic = time.time()
     B = simple_feature(A)
     toc = time.time()
     print("Computing time numpy: {} ms.".format((toc - tic) * 1e3))
     tic = time.time()
     B_ = simple_featureL(list(A))
     toc = time.time()
     print("Computing time list: {} ms.".format((toc - tic) * 1e3))
     print(f'B==B_ is {list(B)==B_}')

if __name__ == "__main__":
    test()