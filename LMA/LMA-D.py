import math
def projection_on_set(v,U):
    r"""
    Calculate the scalar (dot) product between two vectors, v1 and v2, of arbitrary length.
    """
    # Your code here
    for i in range (len(U)):
        for j in range (len(U)):
            if i != j:
                assert len(U[i]) == len(U[j])
                assert abs(scalar_product(U[i], U[j])) < 10**(-10)
    
    list1 = [0] * len(U)
    
    for i in range (len(U)):
        list1[i] = (projection(U[i], v))
        
    return tuple(list1)
