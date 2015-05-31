import sieve_basic
import sys
import math
import threading
import time

def threaded_sieve(nums, nthreads):
    def worker(nums, outdict):
        for n in nums:
            outdict[n] = sieve_basic.iprimes_upto(n)

    # Each thread will get 'chunksize' nums and its own output dict
    chunksize = int(math.ceil(nums / float(nthreads)))
    threads = []
    outs = [{} for i in range(nthreads)]

    for i in range(nthreads):
        # Create each thread, passing it its chunk of numbers to factor
        # and output dict.
        t = threading.Thread(
                target=worker,
                args=(range(i * chunksize, (i + 1) * chunksize),
                      outs[i]))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Merge all partial output dicts into a single dict and return it
    return {k: v for out_d in outs for k, v in out_d.iteritems()}


if __name__ == "__main__":
    t = time.time()
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    print len(threaded_sieve(int(sys.argv[1]), int(sys.argv[2]))) 
    t2 = time.time()
    print t2 - t

