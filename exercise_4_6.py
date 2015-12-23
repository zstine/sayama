"""*********************
# Sayama 2015 chapter 4.3 | pg45 | exercise 4.6
# Author: Z. Stine
# Created: 20151223
# Modified: 2015122
# Description: Implementation of the difference equation:
#   x_t = ax_(t-1) + b, x_0 = 1
*********************"""

from pylab import *

def observe(x, result):
    result.append(x)

def update(a, x):
    next_x = (a * x) + b
    return next_x

if __name__ == "__main__":
    a = 1.1
    b = 5
    x = 1
    result = [x]
    
    for t in xrange(30):
        x = update(a, x)
        observe(x, result)
    print(result)
    plot(result)
    show()
