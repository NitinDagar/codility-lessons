def solution(A):
    s = sum(A)
    out = 0
    m = 0

    for i in A:
        if i==0:
            out = out+s-m
        m = m+i

    if out>1000000000:
        return -1
    
    return out
