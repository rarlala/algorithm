def solution(k, tangerine):
    dict = {}
    
    for t in tangerine:
        if t in dict:
            dict[t] = dict[t] + 1
        else:
            dict[t] = 1
    
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: -item[1])}
    
    answer = 0
    for a, b in dict.items():
        answer += 1
        k -= b
        if k <= 0:
            return answer