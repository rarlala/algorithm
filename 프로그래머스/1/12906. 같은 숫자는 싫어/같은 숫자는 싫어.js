function solution(arr) {
    const answer = [arr[0]]
    
    let prevNum = arr[0]
    for (let i = 1; i <= arr.length - 1; i++){
        if (prevNum !== arr[i]) {
            prevNum = arr[i]
            answer.push(arr[i])
        }
    }
    
    return answer
}