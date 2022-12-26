def cube_root_list(a,e,x0):
    # Your code here
    assert a > 0
    assert e > 0
    assert x0 > 0 
    
    XN = x0 
    N = 0 
    
    cuberoot = [XN]
    
    # condition is in absolute value where it stops when e is more than condiiton 
    # negation of less is more than or equals to (>=)
    while abs((XN ** 3) - a) >= e:
        
        #formula 
        XN = 1/3 * ((2 * XN) + (a / (XN ** 2))) 
        cuberoot.append(XN)
        
        N += 1 
        
    return cuberoot
