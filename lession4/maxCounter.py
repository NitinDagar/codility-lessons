def solution(N, A):
    out = [0]*N
    maxx = 0
    maxxChange = False
    for i in range(len(A)):
        if A[i] <= N:
            out[A[i]-1] = out[A[i]-1]+1
            if(out[A[i]-1]>maxx):
                maxx = out[A[i]-1]
                maxxChange = True
        if A[i] == N+1 and maxxChange:
            out = [maxx]*N
            maxxChange = False
    
    return(out)
