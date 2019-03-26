# from kaggle tutorial on functions 

from time import time

def time_call(fn, arg):
    """Return the amount of time the given function takes (in seconds) when called 
    with the given argument.
    """
    t0 = time()
    fn(arg)
    t1 = time()
    elapsed = t1 - t0
    return elapsed
	
	
def slowest_call(fn, arg1, arg2, arg3):
    """Return the amount of time taken by the slowest of the following function
    calls: fn(arg1), fn(arg2), fn(arg3)
    """
    return max(time_call(fn, arg1), time_call(fn, arg2), time_call(fn, arg3))
