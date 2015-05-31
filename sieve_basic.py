import sys
import time
"""
def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in xrange(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): # start at ``n`` squared
                is_prime[i] = False
    for i in xrange(limit + 1):
        if is_prime[i]: yield i
"""


def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

if __name__ == "__main__":
    t = time.time()
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    res = {} 
    for i in range(int(sys.argv[1])):
        res[i] = iprimes_upto(i)
    t2 = time.time()
    print t2 - t


