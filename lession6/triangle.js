function solution(A) {
    
    o = {}
    out = 0
    m = []

    for(let i=0;i<A.length;i++){
        if (o[A[i]]){
            o[A[i]] = o[A[i]]+1
        }else{
            o[A[i]] = 1
        }
    }

    for(let i in o){
        for(let j=0;j<o[i];j++){
            m.push(Number(i))
        }
    }
    o = m

    for(let i=0;i<o.length-2;i++){

        if(o[i]+o[i+1]>o[i+2] && o[i+1]+o[i+2]>o[i] && o[i+2]+o[i]>o[i+1]){
            return 1
            break
        }
    }
    return 0
}
