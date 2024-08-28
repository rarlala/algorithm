def solution(n):
    num = n
    c2 = format(n, 'b').count('1')
    
    while True:
        num += 1
        c = format(num, 'b').count('1')
        if c == c2:
            return num