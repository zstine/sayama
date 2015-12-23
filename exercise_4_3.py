"""*********************
# Sayama 2015 4.3 pg39
# Author: Z. Stine
# Created: 20151223
# Modified: 2015122
# Description: Example of simulating discrete-time models with one variable using the equation:
#   x_t = ax_(t-1)
*********************"""
from pylab import *

def initialize():
    return 1., [1.]

def observe(x, result):
    result.append(x)

def update(a, x):
    x = a * x
    return x

if __name__ == "__main__":
    a = 1.1
    x, result = initialize()
    
    for t in xrange(30):
        x = update(a, x)
        observe(x, result)
    print(result)
    plot(result)
    show()
