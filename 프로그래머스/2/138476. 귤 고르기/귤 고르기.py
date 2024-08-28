from collections import defaultdict

def solution(k, tangerine):
    dict = defaultdict(int)
    
    for t in tangerine:
        dict[t] += 1
    
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: -item[1])}
    
    answer = 0
    for _, b in dict.items():
        answer += 1
        k -= b
        if k <= 0:
            return answer