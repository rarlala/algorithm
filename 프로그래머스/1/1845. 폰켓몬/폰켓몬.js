function solution(nums) {
    var answer = 0;
    const dict = {}
    
    nums.forEach((n) => {
        if (dict[n]) {
            dict[n] += 1
        } else {
            dict[n] = 1            
        }
    })
    
    const kind = Object.keys(dict).length
    const maxCount = parseInt(nums.length / 2)
    return maxCount < kind ? maxCount : kind
}