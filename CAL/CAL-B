import math
def pn(n,x):

    # Your code here
    finalbernoulli = 0 
    
    for k in range(1,n+1):
        first = bernoulli(2*k) / math.factorial(2*k)
        second = ((-4)**k) 
        third = (1 - (4**k))
        fourth = x ** ((2*k) - 1)
        finalbernoulli += first * second * third * fourth 
    return finalbernoulli 
