import math
def projection_orthogonal(u,v):
    # v onto u 
    # input values are tuples
    assert (isinstance(u, (tuple)))
    assert (isinstance(v, (tuple)))
    
    # same length of tuple
    assert len(u) == len(v)
    
    proj = projection(u,v)
    
    orthogonal = [] 
    
    for i in range(len(u)):
        result = v[i] - proj[i]
        orthogonal.append(result)
    return tuple(orthogonal) 
