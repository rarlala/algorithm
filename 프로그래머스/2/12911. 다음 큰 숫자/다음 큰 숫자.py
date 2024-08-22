def solution(n):
    answer = 0
    num = n + 1
    c2 = format(n, 'b').count('1')
    
    while answer == 0:
        c = format(num, 'b').count('1')
        if c == c2:
            answer = num
        else:
            num += 1
            
    return answer