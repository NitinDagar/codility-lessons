def solution(A):
    max1 = float("-inf")
    max2 = float("-inf")
    max3 = float("-inf")
    nMax1 = float("inf")
    nMax2 = float("inf")

    for i in A:
        if i>max1:
            max3,max2,max1 = max2,max1,i

        elif i>max2:
            max3,max2 = max2,i

        elif i>max3:
            max3 = i
        
        if i<nMax1:
            nMax2,nMax1 = nMax1,i

        elif i<nMax2:
            nMax2 = i

    k = max1*max2*max3
    l = max1*nMax1*nMax2
    
    return max(k,l)
    
