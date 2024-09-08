from itertools import islice

def solution(t, p):
    answer = 0
    
    arrs = zip(*(islice(list(t), i, None) for i in range(len(p))))
    for arr in arrs:
        if int("".join(arr)) <= int(p):
            answer += 1
    
    return answer