import math

def projection(u,v):

    # input values are tuples
    assert (isinstance(u, (tuple)))
    assert (isinstance(v, (tuple)))
    
    # same length of tuple
    assert len(u) == len(v)
    
    # input u is not zero vector 
    assert u != 0 
    
    # Calculation 
    projection = [] 
    
    temp = scalar_product(u,v)
    temp2 = scalar_product(u,u)
    
    for i in range(len(u)):
        newproj = (temp / temp2) * u[i]
        projection.append(newproj)
    return tuple(projection)
