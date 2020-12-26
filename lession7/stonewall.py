out = 0
def solution(H):
    # not efficient 78%

    global out

    def rec(a):

        global out

        arr = []

        c = 0
        t = 0

        m = min(a)

        if(m==0):
            return
        
        for i in range(len(a)):
            a[i] = a[i]-m

            if(a[i]>0 and c==0):
                t = i
                c = 1
            
            if(a[i]==0 and i>0 and c!=0):
                arr.append(a[t:i])
                c=0

        arr.append(a[t:len(a)])

        out = out +1

        for i in arr:
            rec(i)
    
    rec(H)

    return out
