def solution(a, b, n):
    answer = 0
    
    while (n >= a):
        change = n // a * b
        n = change + (n % a)
        answer += change
        
    return answer