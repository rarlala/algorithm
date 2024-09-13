def solution(sizes):
    w, h = 0, 0
    
    for [a, b] in sizes:
        if a > b:
            a, b = b, a
            
        w = max(w, a)
        h = max(h, b)
    
    return w * h