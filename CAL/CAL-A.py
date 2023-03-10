// Write a program which uses the formula above to compute the Bernoulli number ðĩð. Bm for 0 âĪð âĪ12 0 âĪm âĪ12. 

import math
def bernoulli(m):
    # Your code here. 
    assert m in range(0, 13)
    k = 0 
    finalbernoulli = 0
    # ðĩð=ââðâ1ð=0(ðCð)ðĩð/ (ðâð+1)
    
    # B0 equals to 1 
    if m == 0:
        finalbernoulli = 1
        return finalbernoulli 
    else:
        # Calculation of Bernoulli  
        while (k <= m - 1):
            finalbernoulli += -(math.comb(m, k) * (bernoulli(k) / (m - k + 1)))
            k += 1
        
    # Call final result 
    return finalbernoulli
