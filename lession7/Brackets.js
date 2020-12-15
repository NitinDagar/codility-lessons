function solution(S) {

    if(S.length==0){
        return 1
    }

    s = {"}":"{",")":"(","]":"["}
    k = ""

    for (let i of S){
        
        if (i=="(" || i=="{" || i=="["){
            k = k+i
        }
        else if(s[i] == k[k.length-1]){
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
