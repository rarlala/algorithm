let T = Int(readLine()!)!

for _ in 0..<T {
    let N = Int(readLine()!)!
    var result = (0, 0)
    
    if N >= 3 {
        var fibo_count = [(Int, Int)](repeating: (0, 0), count: N + 1)
        fibo_count[0] = (1, 0)
        fibo_count[1] = (0, 1)
        fibo_count[2] = (1, 1)
        
        for i in 3...N {
            fibo_count[i] = (fibo_count[i - 2].0 + fibo_count[i - 1].0, fibo_count[i - 2].1 + fibo_count[i - 1].1)
        }
        
        result = fibo_count[N]
    } else if N == 0 {
        result = (1, 0)
    } else if N == 1 {
        result = (0, 1)
    } else if N == 2 {
        result = (1, 1)
    }
    
    print("\(result.0) \(result.1)")
}