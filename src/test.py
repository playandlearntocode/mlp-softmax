import sys, math
import random
import numpy as np

v1 = np.array([0.1, 0.9])
v2 = np.array([0.1, 0.9])

print('l2')
print(np.log(v2))
print(v1.shape)
print(v2.shape)
print('matmul:')


def loss_function( target_distribution, computed_distribution):
    cross_entropy = - (np.matmul(target_distribution, np.log(computed_distribution)))
    return cross_entropy

print('loss:')
print(loss_function(v1,v2))
