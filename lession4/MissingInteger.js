function solution(A) {
    ret = {}
    for(let i of A){
        ret[i] = true
    }
    k = 1
    while(true){
        if( !ret[k]){
            return k
        }
        k++
    }
}
