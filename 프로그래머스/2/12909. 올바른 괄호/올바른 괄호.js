function solution(s){
    let count = 0
    
    for(let d of s) {
        d === '(' ? count += 1 : count -= 1
        if (count < 0) return false
    }
    
    return count === 0 ? true : false
}