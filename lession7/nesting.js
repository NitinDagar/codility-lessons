function solution(S) {

    // not efficient only 87% pass

    if(S.length==0){
        return 1
    }

    if(S.length%2==1){
        return 0
    }

    k = ""

    for (let i of S){
        
        if (i=="("){
            k = k+i
        }
        else if("(" == k[k.length-1]){
            k = k.slice(0, -1);
        }
        else{
            return 0
        }
    }

    if(k.length){
        return 0
    } 
    
    return 1

}
