function solution(progresses, speeds) {
    const days = progresses.map((p, i) => {
        return Math.ceil((100 - p) / speeds[i])
    })
    
    const results = []
    let prevTime = days.shift()
    let count = 1
    
    days.forEach(d => {
        if (prevTime >= d) {
            count += 1
        } else {
            results.push(count)
            prevTime = d
            count = 1
        }
    })
    
    results.push(count)
    return results
}