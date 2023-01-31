#Gradient Descent vs Stochastic Gradient Descent
# target : x+1
# Conclusion : gd is more stable and accurate in general; sgd saves time and sometimes performs 
# a little better than gd in small test dataset 

import numpy as np
import time
# X = np.linspace(-10.0, 10.0, num=2000)   old version
# data = np.asarray([(x,x+1) for x in X])
# np.random.shuffle(data)
# trainSet = data[:1600]
# testSet = data[1600:]
# num_train = 1600
# MSE = np.mean((y-f(x))**2)

X = np.linspace(-10.0, 10.0, num=2000*2000)   # new version
data = np.asarray([(x,x+1) for x in X])
np.random.shuffle(data)
trainSet = data[:1600*2000]
testSet = data[1600*2000:]
num_train = 1600*2000


def gd(lr=1e-4,epochs=1000):
    params = {}
    grads = {}
    params['w'],params['b'] = 0.,0.
    t1 = time.time()
    for i in range(epochs):
        error = params['w']*trainSet[:,0]+params['b'] - trainSet[:,1] # wx+b-y
        grads['w'] = error.dot(trainSet[:,0])/num_train
        grads['b'] = error.mean()
        for k in params:
            params[k] -= lr*grads[k]
    t2 = time.time()
    print(t2-t1)
    print(params['w'],params['b'])
    model = lambda x:params['w']*x+params['b']
    return model


def sgd(lr=1e-4,epochs=1000,batchSize=1): # 加batch后明显比sample 1个点 要慢
    params = {}
    grads = {}
    params['w'],params['b'] = 0.,0.
    t1 = time.time()
    for i in range(epochs):
        #sample = trainSet[np.random.randint(0,num_train)] version 1 without batch
        randnum = batchSize*np.random.randint(0,num_train//batchSize)  # version 2 with batch
        batch = trainSet[randnum:randnum+batchSize]
        # error = params['w']*sample[0]+params['b'] - sample[1] # wx+b-y
        # grads['w'] = error*sample[0]
        # grads['b'] = error
        error = params['w']*batch[:,0]+params['b'] - batch[:,1] # wx+b-y
        grads['w'] = error.dot(batch[:,0])/batchSize
        grads['b'] = error.mean()
        for k in params:
            params[k] -= lr*grads[k]
    t2 = time.time()
    print(t2-t1)
    print(params['w'],params['b'])
    model = lambda x:params['w']*x+params['b']
    return model

def test(f1,f2):
    num_test = 400
    err1,err2 = 0.,0.
    for i in range(num_test):
        err1 += abs(f1(testSet[i,0])-testSet[i,1])
        err2 += abs(f2(testSet[i,0])-testSet[i,1])
    print(err1,err2)

''' mini-batch version   train 1600  test 400
>>> from gd_sgd import *      
>>> fgd = gd(1e-3,int(1e4))
0.09159040451049805
0.9999999982823551 0.9999548249156524
>>> fsgd = sgd(1e-3,int(1e4))
0.0889279842376709
1.0000020651224764 0.9999545924618897
>>> test(fgd,fsgd)
0.0180700370729584 0.018159006902295327
>>> fsgd = sgd(1e-3,int(1e4))
0.08043193817138672
0.999999522426026 0.9999571618593369
>>> test(fgd,fsgd)
0.0180700370729584 0.0171361832222493
>>> fsgd = sgd(1e-3,int(1e4),100)
0.0851292610168457
0.9999999458893354 0.999954872811264
>>> test(fgd,fsgd)
0.0180700370729584 0.018050980521622906
'''

''' sample version 每次只取一个样本  train 1600 test 400
>>> from gd_sgd import *
>>> sgd(1e-3,int(1e4))
0.02893829345703125
0.9999988826180737 0.9999556495222978
<function sgd.<locals>.<lambda> at 0x00000254800F3E20>
>>> gd(1e-3,int(1e4))  
0.09668564796447754
1.0000000407638916 0.9999548552780525
<function gd.<locals>.<lambda> at 0x00000254A0C5D120>
>>> fsgd = sgd(1e-3,int(1e4))
0.028861284255981445
0.999999856183323 0.9999536142588723
>>> fgd = gd(1e-3,int(1e4))   
0.09667277336120605
1.0000000407638916 0.9999548552780525
>>> fgd(3)
3.999954977569727
>>> fsgd(3)
3.999953182808841
>>> exit(0)

>>> from gd_sgd import *
>>> fgd = gd(1e-3,10000)
0.09763121604919434
1.000000051929522 0.9999548592601436
>>> fsgd = sgd(1e-3,10000)
0.03043389320373535
0.999999570181389 0.9999549728803109
>>> test(fgd,fsgd)
0.018059400803236425 0.017985149066036543
>>> 1-1.000000051929522
-5.192952201582557e-08
>>> 1-0.999999570181389
4.2981861103630337e-07
>>> exit()
'''

''' mini-batch version   train 1600*2000  test 400*2000 这时才显示出mini-batch比full batch要快
当然, full-batch 精度明显更高
>>> from gd_sgd import *      
>>> fsgd = sgd(1e-3,int(1e4),100) 
0.09488320350646973
0.9999999832909886 0.9999547421560488
>>> fgd = gd(1e-3,int(1e4))      
249.34087562561035
0.9999999990756538 0.9999548257235924
>>> test(fgd,fsgd)
0.018069843558972343 0.01810554169114509
>>> 1-0.9999999832909886
1.670901139672054e-08
>>> 1-0.9999999990756538
9.24346155173339e-10
'''

'''
以上训练 还反映出一个问题: bias 的 精度提升明显落后于 weight '''