import sys, math
import random
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([10, 20, 30])

print(v1.shape)
print(v2.shape)
print('matmul:')


def loss_function( target_distribution, computed_distribution):
    cross_entropy = - (np.matmul(target_distribution, np.log(computed_distribution)))
    return cross_entropy

print('loss:')
print(loss_function(v1,v2))

gradient_value = \
    -1 * \
    (
            2
    ) \
    - 1 * \
    (
           3
    )

print ('gv= ')
print(gradient_value)