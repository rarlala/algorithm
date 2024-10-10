def solution(a, b, n):
    answer = 0
    cola = n
    
    while (cola >= a):
        change = cola // a * b
        cola = change + (cola % a)
        answer += change
        
    return answer