def solution(s):
    zero_count = 0
    count = 0
    
    while s != '1':
        zero_count += list(s).count('0')
        s = format((len("".join(s.split("0")))),  'b')
        count += 1
        
    return [count, zero_count]