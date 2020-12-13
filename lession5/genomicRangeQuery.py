def solution(S, P, Q):
    l = len(P)
    sett = {'A':1,'C':2,'G':3,'T':4}
    out = []
    for i in range(l):
        s = S[P[i]:Q[i]+1]
        for j in sett:
            if(j in s):
                out.append(sett[j])
                break
    return out
    pass
