def solution(s):
    zero = 0
    count = 0
    
    while s != '1':
        arr = list(s)
        zero += arr.count('0')
        s = format((len("".join(s.split("0")))),  'b')
        count += 1
        
    return [count, zero]