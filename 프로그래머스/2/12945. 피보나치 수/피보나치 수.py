def solution(n):
    answer = 0
    x, y = 0, 1
    
    for i in range(2, n + 1):
        answer = x + y
        x = y
        y = answer

    return answer % 1234567