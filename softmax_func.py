import numpy as np


def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([1010, 1000, 990])

print(softmax(a))

c = np.max(a)
print(a - c)

y = np.exp(a - c) / np.sum(np.exp(a - c))
print(y)
