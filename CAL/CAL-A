// Write a program which uses the formula above to compute the Bernoulli number 𝐵𝑚. Bm for 0 ≤𝑚 ≤12 0 ≤m ≤12. 

import math
def bernoulli(m):
    # Your code here. 
    assert m in range(0, 13)
    k = 0 
    finalbernoulli = 0
    # 𝐵𝑚=−∑𝑚−1𝑘=0(𝑚C𝑘)𝐵𝑘/ (𝑚−𝑘+1)
    
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
