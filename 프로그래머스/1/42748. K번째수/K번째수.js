function solution(array, commands) {
    const results = []
    commands.forEach((data) => {
        results.push(array.slice(data[0] - 1, data[1]).sort((a, b) => a - b)[data[2] - 1])
    })
    return results
}