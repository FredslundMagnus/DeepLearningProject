# & C:/Users/magnu/Anaconda3/python.exe c:/Users/magnu/Documents/Projects/DeepLearningProject/speed.py

import time
import numpy as np
from numpy.random import default_rng
import random
rng = default_rng()

n = 1000
m = 200000
k = 200
distribution = np.ones(m) / m

# t0 = time.time()
# for i in range(n):
#     rng.choice(m, k, p=distribution)
# t1 = time.time()
# print('RNG', t1 - t0)

# rnd = np.random
# t0 = time.time()
# for i in range(n):
#     rnd.choice(m, k, p=distribution)
# t1 = time.time()
# print('RND', t1 - t0)

# n = 10000

# distribution = np.ones(m) / n

# li = np.arange(m)
# t0 = time.time()
# for i in range(n):
#     slut = random.randint(n, m)
#     rng.choice(li[slut - n:slut], k, p=distribution[slut - n:slut])
# t1 = time.time()
# print('RND 10000', t1 - t0)

# li = np.arange(m)
# t0 = time.time()
# for i in range(n):
#     slut = random.randint(n, m)
#     distPart = distribution[slut - n:slut]
#     rng.choice(np.arange(slut - n, slut), k, p=distPart / distPart.sum())
# t1 = time.time()
# print('RND', t1 - t0)


n = 2000

distribution = np.ones(m) / n

# li = np.arange(m)
# t0 = time.time()
# for i in range(n):
#     slut = random.randint(n, m)
#     rng.choice(li[slut - n:slut], k, p=distribution[slut - n:slut])
# t1 = time.time()
# print('RND', t1 - t0)

li = np.arange(m)
distribution = np.ones(m) / m
t0 = time.time()
for i in range(n):
    slut = random.randint(n, m)
    distPart = distribution[slut - n:slut]
    rng.choice(np.arange(slut - n, slut), k, p=distPart / distPart.sum())
t1 = time.time()
print('RND 2000', t1 - t0)


# m = 200000
# distribution = np.ones(m) / m
# rnd = np.random
# t0 = time.time()
# for i in range(n):
#     rnd.choice(m, k, p=distribution)
# t1 = time.time()
# print('m = 200000', t1 - t0)

# m = 20000
# distribution = np.ones(m) / m
# rnd = np.random
# t0 = time.time()
# for i in range(n):
#     rnd.choice(m, k, p=distribution)
# t1 = time.time()
# print('m = 200000', t1 - t0)

m = 2000
distribution = list(np.ones(m) / m)
rnd = np.random
t0 = time.time()
for i in range(n):
    rnd.choice(m, k, p=distribution)
t1 = time.time()
print('m = 200000', t1 - t0)


m = 200000
distribution = list(range(m))
t0 = time.time()
for i in range(n):
    random.sample(distribution, k)
t1 = time.time()
print('m = 200000', t1 - t0)

print(bool(0.0))
print(bool(1.0))
print(bool(0.1))
print(bool(int(0.0)))
print(bool(int(1.0)))
print(bool(int(0.1)))
