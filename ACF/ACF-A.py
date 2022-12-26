def cube_root(a,e,x0):
    # Your solution here
    
    # assert that a, e, x0 are positive numbers are positive numbers.
    assert a > 0
    assert e > 0
    assert x0 > 0 
    
    XN = x0 
    N = 0 
    
    # condition is in absolute value where it stops when e is more than condiiton 
    # negation of less is more than or equals to (>=)
    while abs((XN ** 3) - a) >= e:
        
        #formula 
        XN = 1/3 * ((2 * XN) + (a / (XN ** 2))) 
        
        N += 1 
        
    return (XN, N) 
