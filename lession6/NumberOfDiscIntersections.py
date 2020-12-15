def solution(A):
    # Not Efficient

    out = 0

    for i in range(len(A)):
        for j in range(i+1,len(A)):    
           if j-A[j] <= A[i]+i:
               out = out+1    
    return out
    pass
