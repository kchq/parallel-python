import sys
import math
import multiprocessing
import sieve_basic
from Queue import Queue
import time

def paralleled_sieve(nums, nprocs):
    def worker(nums, outs):
        """ The worker function, invoked in a process. 'nums' is a
            list of numbers to factor. The results are placed in
            a dictionary that's pushed to a queue.
        """
        outdict = {}
        for n in nums:
            outdict[n] = sieve_basic.iprimes_upto(n)
        outs.put(outdict)

    # Each process will get 'chunksize' nums and a queue to put his out
    # dict into
    outs = Queue() 
    chunksize = int(math.ceil(nums / float(nprocs)))
    procs = []

    for i in range(nprocs):
        p = multiprocessing.Process(
                target=worker,
                args=(range(i * chunksize, (i + 1) * chunksize),
                      outs))
        procs.append(p)
        p.start()

    # Collect all results into a single result dict. We know how many dicts
    # with results to expect.
    resultdict = {}
    for i in range(nprocs):
        #print outs.get()
        #resultdict.update(outs.get())
        pass
    

    # Wait for all worker processes to finish
    for p in procs:
        p.join()

    print outs 
    return resultdict

if __name__ == "__main__":
    t = time.time()
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    print len(paralleled_sieve(int(sys.argv[1]), int(sys.argv[2])))
    t2 = time.time()
    print t2 - t

