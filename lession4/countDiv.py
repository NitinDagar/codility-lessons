def solution(A, B, K):

    if A==0:
        return int(B/K) + 1
    return int(B/K) - int((A-1)/K)
    pass
