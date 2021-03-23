function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)

    ret = {}

    for(let i in A){
        if(ret[A[i]]){
            ret[A[i]].count += 1
        } else{
            ret[A[i]] = {
                index:i,
                count:1
            }
        }
    }

    for(let i in ret){
        if(ret[i].count>(A.length/2)){
            return Number(ret[i].index)
        }
    }
    return -1
}
