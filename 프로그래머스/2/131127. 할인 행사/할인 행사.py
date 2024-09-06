from collections import Counter
from itertools import islice

def solution(want, number, discount):
    answer = 0
    dict = {}
    for w, n in zip(want, number):
        dict[w] = n
        
    ten_days = zip(*(islice(discount, i, None) for i in range(10)))
    
    for ten_day in ten_days:
        y_counter = Counter(ten_day)
        answer += 1 if all(dict[a] == y_counter[a] for a in dict) else 0
    
    return answer