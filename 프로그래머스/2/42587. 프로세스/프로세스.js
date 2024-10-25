function solution(priorities, location) {
    const queue = priorities.map((value, index) => ({index, value}))
    let order = 0
    
    while (queue.length) {
        const current = queue.shift()
        
        if (queue.some(item => item.value > current.value)) {
            queue.push(current)
        } else {
            order++;
            if (current.index === location) {
                return order
            }
        }
    }
}