function solution(progresses, speeds) {
    const days = progresses.map((p, i) => {
        return Math.ceil((100 - p) / speeds[i])
    })
    
    const results = []
    let prevTime = days.shift()
    let count = 1
    
    while(days.length) {
        let currentTime = days.shift()
        if (prevTime >= currentTime) {
            count += 1
        } else {
            results.push(count)
            prevTime = currentTime
            count = 1
        }
        
        if (days.length === 0) {
            results.push(count)
        }
    }
    
    return results
}