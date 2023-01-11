def scalar_product(v1,v2):
    
    # Your code here
    
    # input values are tuples 
    assert (isinstance(v1, (tuple)))
    assert (isinstance(v2, (tuple)))
  
    # length of v1 and v2 are the same 
    assert len(v1) == len(v2)
    
    # containing only int or float
    assert (isinstance(vector, (int, float)) for vector in v1)
    assert (isinstance(vector, (int, float)) for vector in v2)
    
    # Calculation 
    
    # Begin with ensuring that variable dot is empty 
    dot = 0 
    
    # Loop through all elements of either v1 or v2 
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
    return dot 
