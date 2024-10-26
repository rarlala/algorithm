function solution(sizes) {
    let row = 0, col = 0
    
    sizes.forEach((size) => {
        const [r, c] = size.sort((a, b) => a - b)
        
        if (row < r) row = r
        if (col < c) col = c
    })
    
    return row * col
}