def solution(A, B):

    # not efficient 50%

    f = 0
    fs = 0
    lf = len(A)


    for i in range(len(A)):
        if B[i]==1:
            if A[i]>fs:
                fs = A[i]
            f = f+1
        
        if B[i]==0 and fs>0:
            if A[i]>fs:
                lf = lf - f
                f = 0
            else:
                lf = lf -1
    
    return lf
    pass
