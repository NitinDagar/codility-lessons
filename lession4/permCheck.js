
function solution(A) {
    ret = {}
    for(let i of A){
        ret[i] = true
    }
    let max = A.length
    while(true){
        if( !ret[max]){
            return 0
        }
        max--
        if(max == 0){
            return 1
        }
    }
}
